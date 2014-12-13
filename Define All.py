# from xml.etree import ElementTree
# from xmlutils.xml2json import xml2json
import xmltodict, json
import requests

def get_def(word):
	#url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/' + str(word) + '?key=3b0ab062-83f3-44dd-8a38-77641fc48664'
	url = 'http://api.wordnik.com/v4/word.json/' + str(word).lower() + '/definitions?limit=200&includeRelated=true&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
	response = requests.get(url).text
	response = json.loads(response)[0]['text']
	definition = response


	# doc = xmltodict.parse(response.text)
	# data = json.loads(json.dumps(doc))
	# print(json.dumps(data, sort_keys=True,indent=4, separators=(',', ': ')))

	# definition = data['entry_list']['entry']['def']['dt'][1][1:].capitalize()

	return definition
	# print(definition)
	# converter = xml2json(response.text)
	# print (converter.get_json())

	# data = ElementTree.fromstring(response.content)
print("Input a list of words\n")
word_list = input().split(', ')
print('\n')
for word in word_list:
	print(word.capitalize() + " : " + get_def(word) + '\n') 
