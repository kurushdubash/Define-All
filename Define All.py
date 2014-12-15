import requests, json

def get_def(word):
	url = 'http://api.wordnik.com/v4/word.json/' + str(word) + '/definitions?limit=1&includeRelated=true&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
	try: 
		response = requests.get(url).text
		response = json.loads(response)[0]
		definition = response['text']
	except IndexError:
		definition = 'No definitions found.'
	except:
		definition = 'FAILED --- Something went wrong.'
	return definition

print("Input a list of words\n")
word_list = input()
if ',' in word_list:
	word_list=word_list.split(', ')
else:
	word_list=word_list.split()
print('\n')
for word in word_list:
	print(word + " : " + get_def(word) + '\n') 
