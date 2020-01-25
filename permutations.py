"""
For God Through Christ
Jacob Webb

Purpose: Create all permutations of words that the user enters.
Design: Recursively parse out a word into all permutations of strings.
	Break into minumum word length and check against a dictionary to return
	only actual words.
"""

from flask import Flask 
from flask import request 
from flask import render_template
from flask import session 
from flask import url_for
import json
app = Flask(__name__)

# Load dictionary into the program and store in dict_file
def loadDictionary(file_name):
	dict_file = open(file_name, "r").read().splitlines()
	return dict_file

# from a given set of letters give all possible 'words'
def getPermutations(my_word):
	perm_list = []
	# Recursive function that returns all from 1 letter to all letters and all combinations of these
	if (len(my_word) == 0):	
		return perm_list
	if (len(my_word) == 1):			# add a one letter word and put it in the 
		perm_list.append(my_word)
		return perm_list
	else:
		for i, letter in enumerate(my_word):		# for each letter in the 'word'
			my_letter = my_word[i]					
			perm_list.append(my_letter)				# start a list with the ith letter
			sub_word = my_word[ : i] + my_word[i + 1 : ]	# return word without my_letter
			new_list = getPermutations(sub_word)	# recursively get smaller and smaller combinations of letters
			for k, word in enumerate(new_list):
				new_list[k] = new_list[k] + my_letter	# add the ith letter back to the kth word to complete the word
			perm_list = perm_list + new_list
		return perm_list

dict_set = set(loadDictionary("en-US.dic"))

@app.route("/")
def index():
	return render_template("index.html")


@app.route('/permutations', methods=['POST'])
def index_post():
	my_word = request.form['my_word']
	permutations_list = getPermutations(my_word)	
	word_list = []
	word_limit = int(request.form['word_length'])

	for element in permutations_list:
		if((len(element) >= word_limit) and (element in dict_set)):
			word_list.append(element)

	#get word_list as a set to eliminate duplicates then set as a list again for data container
	word_set = list(set(word_list))

	# return list to ajax call, remove brackets from python list first
	return json.dumps(word_set).strip('[]')

if __name__ == '__main__':
	app.run()
