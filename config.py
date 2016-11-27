# -*- coding: utf-8 -*-
out_dir = './out/' # trailing slash required
user_agent = 'stw2openmensa (https://github.com/chk1/stw2openmensa)'

base_url = 'http://speiseplan.stw-muenster.de/'
canteen_files = [
	'mensa_aasee.xml',
	'mensa_am_ring.xml',
	'mensa_bispinghof.xml',
	'mensa_da_vinci.xml',
	'mensa_steinfurt.xml',
	'bistro_coerdehof.xml',
	'bistro_denkpause.xml',
	'bistro_durchblick.xml',
	'bistro_frieden.xml',
	'bistro_huefferstift.xml',
	'bistro_kabu.xml',
	'bistro_katho.xml',
	'bistro_oeconomicum.xml'
]
additives = {
	# Zusatzstoffe
	'1': 'Farbstoff',
	'2': 'Konservierungsstoff',
	'3': 'Antioxidationsmittel',
	'4': 'Geschmacksverstärker',
	'5': 'geschwefelt',
	'6': 'geschwärzt',
	'7': 'gewachst',
	'8': 'Phosphat',
	'9': 'Süßungsmitteln',
	'10': 'eine Phenylalaninquelle',
	# Allergene
	'A': 'glutenhaltiges Getreide',
	'B': 'Krebstiere',
	'C': 'Ei',
	'D': 'Fisch',
	'E': 'Erdnüsse',
	'F': 'Soja',
	'G': 'Milch',
	'H': 'Schalenfrüchte',
	'I': 'Sellerie',
	'J': 'Senf',
	'K': 'Sesam',
	'L': 'Lupinen',
	'M': 'Weichtiere',
	'N': 'Schwefeldioxid und Sulfite'
}