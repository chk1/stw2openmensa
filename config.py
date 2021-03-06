# -*- coding: utf-8 -*-
OUT_DIR = './out/' # trailing slash required
USER_AGENT = 'stw2openmensa (https://github.com/chk1/stw2openmensa)'

BASE_URL = 'http://speiseplan.stw-muenster.de/'
CANTEEN_FILES = [
	'mensa_aasee.xml',
	'mensa_am_ring.xml',
	'mensa_bispinghof.xml',
	'mensa_da_vinci.xml',
	'mensa_steinfurt.xml',
	#'bistro_coerdehof.xml',
	'bistro_denkpause.xml',
	'bistro_durchblick.xml',
	'bistro_frieden.xml',
	'bistro_friesenring.xml',
	#'bistro_huefferstift.xml',
	'bistro_kabu.xml',
	'bistro_katho.xml',
	'bistro_oeconomicum.xml'
]
ADDITIVES = {
	# Zusatzstoffe
	'1': 'Farbstoff',
	'2': 'Konservierungsstoff',
	'3': 'Antioxidationsmittel',
	'4': 'Geschmacksverstärker',
	'5': 'geschwefelt',
	'6': 'geschwärzt',
	'7': 'gewachst',
	'8': 'Phosphat',
	'9': 'Süßungsmittel',
	'10': 'eine Phenylalaninquelle',
	'15': 'chininhaltig',
	'16': 'koffeinhaltig',
	# Allergene
	'A': 'glutenhaltiges Getreide',
	'ADI': 'Dinkel',
	'AGE': 'Gerste',
	'AHA': 'Hafer',
	'AKA': 'Kamut',
	'ARO': 'Roggen',
	'AWE': 'Weizen',
	'B': 'Krebstiere',
	'C': 'Ei',
	'D': 'Fisch',
	'E': 'Erdnüsse',
	'F': 'Soja',
	'G': 'Milch',
	'H': 'Schalenfrüchte',
	'HMA': 'Mandeln',
	'HHA': 'Haselnüsse',
	'HWA': 'Walnüsse',
	'HCA': 'Cashewkerne/Kaschunüsse',
	'HPE': 'Pecannüsse',
	'HPA': 'Paranüsse',
	'HPI': 'Pistazien',
	'HQU': 'Queenslandnüsse / Macadamianüsse',
	'I': 'Sellerie',
	'J': 'Senf',
	'K': 'Sesam',
	'L': 'Lupinen',
	'M': 'Weichtiere',
	'N': 'Schwefeldioxid und Sulfite',
	# Other
	'Alk': 'Alkohol'
}
CLASSIFICATION = {
	'alk': 'Alkohol',
	'fis': 'Fisch',
	'gfl': 'Geflügel',
	'gefl': 'Geflügel',
	'rin': 'Rind',
	'rnd': 'Rind',
	'sch': 'Schwein',
	'vgn': 'Vegan',
	'vgt': 'Vegetarisch',
	'veg': 'Vegetarisch',
	'bio': 'Bioprodukte'
}
