"""
For God Through Christ
Jacob Webb

Purpose: Create all permutations of words that the user enters.
Design: Recursively parse out a word into all permutations of strings.
	Break into minumum word length and check against a dictionary to return
	only actual words.
"""
"""from tkinter import *

root = Tk()
root.title("All Words")

lb = Listbox()
"""
def loadDictionary(file_name):
	dict_file = open(file_name, "r").read().splitlines()
	return dict_file

def getPermutations(my_word):
	perm_list = []
	if (len(my_word) == 0):
		return perm_list
	if (len(my_word) == 1):
		perm_list.append(my_word)
		return perm_list
	else:
		for i, letter in enumerate(my_word):
			my_letter = my_word[i]
			perm_list.append(my_letter)
			sub_word = my_word[ : i] + my_word[i + 1 : ]	# return word without my_letter
			new_list = getPermutations(sub_word)
			for k, word in enumerate(new_list):
				new_list[k] = new_list[k] + my_letter
			perm_list = perm_list + new_list
		return perm_list

dict_set = set(loadDictionary("en-US.dic"))


quit = "n"

while (quit != "y"):
	word = input("What word would you like to parse? ")

	lb.delete(0, END)
	permutations_list = getPermutations(word)	
	word_list = []
	word_limit = int(input("What is the minimum word size? "))

	for element in permutations_list:
		if((len(element) >= word_limit) and (element in dict_set)):
			word_list.append(element)

	for item in word_list:
		lb.insert(END, item)

	lb.pack()

	quit = input("Would you like to quit? (y or n): \n")

root.mainloop()
