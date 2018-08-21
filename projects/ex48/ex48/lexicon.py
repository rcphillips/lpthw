
def scan(incoming_words):
	# our output is going to be a converted list, going from the word,
	# to word-type tuples
	incoming_words = incoming_words.lower()
	words=incoming_words.split(' ')

	result = []
	for word in words:
		if word in list_of_words:
			result.append((list_of_words[word], word))
		elif type(convert_number(word)) is int:
			result.append(('number', convert_number(word)))
		else:
			result.append(('error', word))
	return result

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		None


list_of_words = {
			'go': 'verb',
			'kill': 'verb',
			'eat': 'verb',
			'the': 'stop',
			'in': 'stop',
			'of': 'stop',
			'north': 'direction',
			'west': 'direction',
			'south': 'direction',
			'east': 'direction',
			'bear': 'noun',
			'princess': 'noun',

			}

first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]

# first thing we're going to do is take user input

# then we're going to split it into pieces

# then we're going to assess each piece

# and finally we're going to return a tuple indicating the 
# type of word, and the word itself.
#these last three seem like they'll be in a function

print(sentence)