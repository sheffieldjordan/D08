#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def store_to_dict():
	words_dict = {} #establish an empty dictionary
	with open("words.txt", "r") as words: #opens the file and assigns 'words' as the file handle
		lines = words.readlines() # converts each line of the file into a list; set that list equal to the lines variable
		for item in lines: #for the objects within 'lines', do the following:
			words_dict[item.strip()] = 0 # strip the characters, then establish them as keys in the empty dictionary, and set their values equal to 0.  
    #store each word in dictionary[key]
	
	return words_dict

###############################################################################
def main():  # DO NOT CHANGE BELOW
    # print(store_to_dict)
    words_dict = store_to_dict()
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()
