import requests

def task3():
	animal_dictionary = {}
	S = requests.Session()
	URL = "https://ru.wikipedia.org/w/api.php"

	PARAMS = {
	    "format": "json",
	    "list": "categorymembers",
	    "action": "query",
	    "cmtitle": "Категория:Животные_по_алфавиту",
		"cmlimit": "500"
	}
	
	while(True):
		R = S.get(url=URL, params=PARAMS)
		DATA = R.json()
		ANIMALS = DATA["query"]["categorymembers"]

		for animal in ANIMALS:
			if animal['ns'] == 0: #считаются только статьи в категории, игнорируются подкатегории и прочие технические страницы
				animal_letter = animal['title'][0]
				if animal_letter in animal_dictionary:
					animal_dictionary[animal_letter] += 1
				else:
					animal_dictionary[animal_letter] = 1

		try:
			PARAMS['cmcontinue'] = DATA['continue']['cmcontinue']
		except KeyError:
			break

	return animal_dictionary


result = task3()
for letter in result:
	print(letter+':',result[letter])
