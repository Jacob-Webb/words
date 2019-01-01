"""
For God Through Christ
Jacob Webb

Purpose: Create all permutations of words that the user enters.
Design: Recursively parse out a word into all permutations of strings.
	Break into minumum word length and check against a dictionary to return
	only actual words.
"""
"""
Removed the tkinter gui
from tkinter import *

root = Tk()
root.title("All Words")

lb = Listbox()
"""
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


quit = "n"

while (quit != "y"):
	word = input("What word would you like to parse? ")

	#lb.delete(0, END)
	permutations_list = getPermutations(word)	
	word_list = []
	word_limit = int(input("What is the minimum word size? "))

	for element in permutations_list:
		# if the word in the list is at least as long as the size limit and if it's found in the dictionary, append it to the final word list
		if((len(element) >= word_limit) and (element in dict_set)):
			word_list.append(element)

	for word in word_list:
		print(word)

	#for item in word_list:
		#lb.insert(END, item)

	#lb.pack()

	quit = input("Would you like to quit? (y or n): \n")

#root.mainloop()
