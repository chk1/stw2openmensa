# -*- coding: utf-8 -*-
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

additives_expr = re.compile(r' \(((?:[0-9a-zA-Z]|10)(?:(?:,(?:[0-9a-zA-Z]|10))+)?)\)')
cleanup_expr   = re.compile(r'\s\s|\(\)|\r?\n')
foodicons_expr = re.compile(r', ?')

def getNote(meal):
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
	fis = foodicons_expr.split(fi)
	try:
		fis = map(lambda x: config.CLASSIFICATION[x], fis)
	except KeyError:
		pass
	return fis

def StudentenwerkToOpenmensa(baseurl, outputdir, user_agent, filename):
	request = urllib2.Request('{}{}'.format(baseurl, filename))
	request.add_header('User-Agent', user_agent)
	opener = urllib2.build_opener()
	mensaXml = opener.open(request).read()

	# studentenwerk source document
	st_soup = BeautifulSoup(mensaXml, 'lxml-xml')

	# openmensa target document
	om_soup = BeautifulSoup('', 'lxml-xml')
	om_root = om_soup.new_tag('openmensa')
	om_root['version'] = '2.1'
	om_root['xmlns'] = 'http://openmensa.org/open-mensa-v2'
	om_root['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'
	om_root['xsi:schemaLocation'] = 'http://openmensa.org/open-mensa-v2 http://openmensa.org/open-mensa-v2.xsd'
	om_soup.append(om_root)

	om_root.append(om_soup.new_tag('canteen'))

	st_menu = st_soup.menue
	# print st_menu['location']
	st_days = st_menu.find_all('date')
	for st_day in st_days:
		mealcounter = 0
		date_day = datetime.fromtimestamp(int(st_day['timestamp'])).strftime('%Y-%m-%d')
		
		om_day = om_soup.new_tag('day', date=date_day)

		# as of now, there is just one item in each category
		st_items = st_day.find_all('item')
		for st_item in st_items:
			# check for empty items
			if st_item.category != None and st_item.price1 != None: 
				# surrounding tags for each meal, again, 1:1 for each meal/category/item
				om_category = om_soup.new_tag('category')
				om_category['name'] = st_item.category.contents[0]

				om_meal = om_soup.new_tag('meal')

				# meal attributes
				om_meal_name = om_soup.new_tag('name')
				om_meal_price1 = om_soup.new_tag('price', role='student')
				om_meal_price2 = om_soup.new_tag('price', role='employee')
				om_meal_price3 = om_soup.new_tag('price', role='other')

				om_meal_name.string = additives_expr.sub('', st_item.meal.contents[0])
				om_meal_name.string = cleanup_expr.sub('', om_meal_name.string).strip()
				om_meal.append(om_meal_name)

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

				# the vegan "Tagesmenu" has no prices, discard 
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
			if mealcounter > 0:
				om_root.canteen.append(om_day)

	with open('{}{}'.format(outputdir, filename), 'w') as out:
		out.write(str(om_soup))

for filename in config.CANTEEN_FILES:
	try:
		print('Processing "{}"'.format(filename))
		StudentenwerkToOpenmensa(config.BASE_URL, config.OUT_DIR, config.USER_AGENT, filename) 
	except Exception as e:
		print('Conversion of "{}" failed: {}'.format(filename, e))
		traceback.print_exc()