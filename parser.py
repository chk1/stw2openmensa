# -*- coding: utf-8 -*-
import os
import stwcanteens
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime

def StudentenwerkToOpenmensa(outputdir, filename):
	response = urllib2.urlopen('http://speiseplan.stw-muenster.de/{}'.format(filename))
	mensaXml = response.read()

	# studentenwerk source document
	st_soup = BeautifulSoup(mensaXml, 'lxml-xml')

	# openmensa target document
	om_soup = BeautifulSoup("", 'lxml-xml')
	om_root = om_soup.new_tag("openmensa")
	om_root['version'] = "2.1"
	om_root['xmlns'] = "http://openmensa.org/open-mensa-v2"
	om_root['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
	om_root['xsi:schemaLocation'] = "http://openmensa.org/open-mensa-v2 http://openmensa.org/open-mensa-v2.xsd"
	om_soup.append(om_root)

	om_root.append(om_soup.new_tag("canteen"))

	st_menu = st_soup.menue
	# print st_menu['location']
	st_days = st_menu.find_all('date')
	for st_day in st_days:
		date_day = datetime.fromtimestamp(int(st_day['timestamp'])).strftime('%Y-%m-%d')
		
		om_day = om_soup.new_tag('day', date=date_day)

		# as of now, there is just one item in each category
		st_items = st_day.find_all('item')
		for st_item in st_items:
			# surrounding tags for each meal, again, 1:1 for each meal/category/item
			om_category = om_soup.new_tag('category')
			om_category['name'] = st_item.category.contents[0]

			om_meal = om_soup.new_tag('meal')

			# meal attributes
			om_meal_name = om_soup.new_tag('name')
			om_meal_note = om_soup.new_tag('note')
			om_meal_price1 = om_soup.new_tag('price', role='student')
			om_meal_price2 = om_soup.new_tag('price', role='employee')
			om_meal_price3 = om_soup.new_tag('price', role='other')

			om_meal_name.string = st_item.meal.contents[0].encode('utf-8')
			om_meal_note.string = ''
			
			price1 = st_item.price1.contents[0]
			price2 = st_item.price2.contents[0]
			price3 = st_item.price3.contents[0]

			# "tagesmenu" for vegan menu, discard entirely
			valid = False
			if price1 != '-' or price2 != '-' or price3 != '-':
				valid = True # hopefully...
				om_meal_price1.string = price1.replace(',', '.')
				om_meal_price2.string = price2.replace(',', '.')
				om_meal_price3.string = price3.replace(',', '.')

				om_meal.append(om_meal_name)
				# om_meal.append(om_meal_note)
				om_meal.append(om_meal_price1)
				om_meal.append(om_meal_price2)
				om_meal.append(om_meal_price3)

				om_category.append(om_meal)
				om_day.append(om_category)
		if valid:
			om_root.canteen.append(om_day)

	with open('{}{}'.format(outputdir, filename), 'w') as out:
		out.write(om_soup.encode('utf-8'))

for file in stwcanteens.CANTEENS:
	try:
		print 'Processing "{}"'.format(file)
		StudentenwerkToOpenmensa('out/', file) # trailing slash on the output directory
	except Error as e:
		print 'Conversion of "{}" failed: {}'.format(file, e)