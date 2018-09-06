# -*- coding: utf-8 -*-
from __future__ import print_function
import config
import re
import os
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import traceback

additives_expr = re.compile(r' ?\(((?:[0-9a-zA-Z]|10|Alk)(?:(?:[,;\.](?:[0-9a-zA-Z]|10|Alk))+)?,?)\)')
cleanup_expr   = re.compile(r'\(\)|\r?\n')
spaces_expr    = re.compile(r'\t|\s\s+')
foodicons_expr = re.compile(r', ?')

def getNote(meal):
	"""
	Meal names contain numbers and letters in parenthesis for declaring additives 
	and warnings for substances that might cause allergic reactions.

	This function parses that information and returns a "human readable" list of ingredients
	which will be inserted in a <note> tag in the resulting XML.

	Example: "(A,B,C,1,2)"
	Expected result: "Enthält Zusatzstoffe: <list>"
	"""
	additive_brackets = additives_expr.findall(meal)
	add_cat1=[] # Zusatzstoffe
	add_cat2=[] # Allergene
	additives_all = ','.join(additive_brackets)
	additives_all = list(set(additives_all.split(',')))
	for x in additives_all:
		try:
		    add_cat1.append(config.ADDITIVES[x]) if x.isdigit() else add_cat2.append(config.ADDITIVES[x])
		except KeyError:
			pass
	result_string_array = []
	if len(add_cat1) > 0:
		cat1_str = 'Enthält Zusatzstoffe: {}'.format(', '.join(add_cat1))
		result_string_array.append(cat1_str)
	if len(add_cat2) > 0:
		cat2_str = 'Enthält Allergene: {}'.format(', '.join(add_cat2))
		result_string_array.append(cat2_str)
	return result_string_array

def getFoodicon(fi):
	"""
	The "foodicons" XML tag depicts a category for a meal, 
	it contains one or more (comma separated) abbreviations for each category

	Example: "<foodicons>Gfl, Alk</foodicons>"
	Expected result: "Geflügel, Alkohol"
	"""
	fis = foodicons_expr.split(fi)
	try:
		fis = map(lambda x: config.CLASSIFICATION[x.lower()], fis)
	except KeyError:
		pass
	return fis

def StudentenwerkToOpenmensa(baseurl, outputdir, user_agent, filename):
	request = urllib2.Request('{}{}'.format(baseurl, filename))
	request.add_header('User-Agent', user_agent)
	opener = urllib2.build_opener()
	mensaXml = opener.open(request).read()

	# Use for debugging: write input files to a folder
	#with open('{}{}'.format("in/", filename), 'w') as out:
	#	out.write(str(mensaXml))

	# Studentenwerk source document prefix "st_"
	st_soup = BeautifulSoup(mensaXml, 'lxml-xml')

	# OpenMensa target document prefix "om_"
	om_soup = BeautifulSoup('', 'lxml-xml')
	om_root = om_soup.new_tag('openmensa')
	om_root['version']            = '2.1'
	om_root['xmlns']              = 'http://openmensa.org/open-mensa-v2'
	om_root['xmlns:xsi']          = 'http://www.w3.org/2001/XMLSchema-instance'
	om_root['xsi:schemaLocation'] = 'http://openmensa.org/open-mensa-v2 http://openmensa.org/open-mensa-v2.xsd'
	om_soup.append(om_root)

	om_root.append(om_soup.new_tag('canteen'))

	st_menu = st_soup.menue
	# print st_menu['location']
	st_days = st_menu.find_all('date')
	for st_day in st_days:
		# canteen might not have any data, skip
		if not st_day.has_attr('timestamp') or st_day['timestamp'] == '':
			continue

		mealcounter = 0
		date_day = datetime.fromtimestamp(int(st_day['timestamp'])).strftime('%Y-%m-%d')
		
		om_day = om_soup.new_tag('day', date=date_day)
		closed_today = False

		# As of now, there is just one item in each category
		# e.g. <item><category>Tagesgericht 1</category> ... </item>
		st_items = st_day.find_all('item')
		for st_item in st_items:

			# Check for empty items
			if st_item.category != None and st_item.price1 != None: 
				# Create surrounding tags for each meal, again, 1:1 for each meal/category/item
				om_category = om_soup.new_tag('category')
				om_category['name'] = st_item.category.contents[0]

				if (st_item.category.contents[0].strip() == "Info"
				    and "geschlossen" in st_item.meal.contents[0].lower()):
					closed_today = True
				else:
					om_meal = om_soup.new_tag('meal')

					# meal attributes
					om_meal_name = om_soup.new_tag('name')
					om_meal_price1 = om_soup.new_tag('price', role='student')
					om_meal_price2 = om_soup.new_tag('price', role='employee')
					om_meal_price3 = om_soup.new_tag('price', role='other')

					om_meal_name.string = additives_expr.sub('', st_item.meal.contents[0])
					om_meal_name.string = spaces_expr.sub(' ', om_meal_name.string)
					om_meal_name.string = cleanup_expr.sub('', om_meal_name.string).strip()
					om_meal.append(om_meal_name)

					""" 
					"food icons" - Meal classification 
					
					Meal classificatins are signified using colored icons on the STW website, apps 
					and public screens.

					In the OpenMensa XML we will put the classification it in a <note> tag instead,
					i.e. "rin" -> Rind, "vgt" -> Vegetarisch etc.
					"""
					if st_item.foodicons != None and len(st_item.foodicons.contents) > 0:
						foodicons = getFoodicon(st_item.foodicons.contents[0])
						for foodicon in foodicons:
							om_meal_note = om_soup.new_tag('note')
							om_meal_note.string = foodicon
							om_meal.append(om_meal_note)

					additives = getNote(st_item.meal.contents[0])
					for additive in additives:
						om_meal_note = om_soup.new_tag('note')
						om_meal_note.string = additive
						om_meal.append(om_meal_note)

					price1 = st_item.price1.contents[0]
					price2 = st_item.price2.contents[0]
					price3 = st_item.price3.contents[0]

					# Discard items with no price (for example, often times vegan "Tagesmenu")
					# because it doesn't fit in the XML model
					if price1 != '-' and price2 != '-' and price3 != '-':
						om_meal_price1.string = price1.replace(',', '.')
						om_meal_price2.string = price2.replace(',', '.')
						om_meal_price3.string = price3.replace(',', '.')

						om_meal.append(om_meal_price1)
						om_meal.append(om_meal_price2)
						om_meal.append(om_meal_price3)

						om_category.append(om_meal)
						om_day.append(om_category)
						mealcounter = mealcounter+1
						closed_today = False

			if not closed_today and mealcounter > 0:
				om_root.canteen.append(om_day)

		# If there are no meals and there is the word "geschlossen" somewhere in the meal's text
		# add a <closed/> tag for the day
		if mealcounter == 0 and closed_today:
			om_closed = om_soup.new_tag('closed')
			om_day.append(om_closed)
			om_root.canteen.append(om_day)

	with open(os.path.join(outputdir, filename), 'w') as out:
		out.write(str(om_soup))
	return "ok"

if __name__ == "__main__":
	if not os.path.isdir(config.OUT_DIR):
		raise Exception("The output folder {} does not exist. please check your configuration file.".format(config.OUT_DIR))

	for filename in config.CANTEEN_FILES:
		try:
			print('Processing "{}" '.format(filename), end='')
			status = StudentenwerkToOpenmensa(config.BASE_URL, config.OUT_DIR, config.USER_AGENT, filename) 
			print(status)
		except Exception as e:
			print('Conversion of "{}" failed: {}'.format(filename, e))
			traceback.print_exc()