#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    keys_list = []
    for key, value  in d.items():
    	if value == v:
    		keys_list.append(key)
    return keys_list

def reverse_lookup_new(d, v):
	keys_list = []
	for key, value in d.items():
		# print(key, value)
		if value == v:
			keys_list.append(key)
	return keys_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_old(s):
    d = dict()
    for key in s: # for each letter in string
        d[key] = 1 + d.get(key, 0) # check to see if the letter is in the dictionary. If not, return 0. Then establish that letter as a value in the dictionary and set the value equal to '0' + 1. 
    return d # return the dictionary with the new letters as keys. 



def histogram_new(pledge_list):
    pledge_dict = {}
    for key in pledge_list:
        pledge_dict[key] = 1 + pledge_dict.get(key, 0) 
    return pledge_dict

    


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    pledge_list = []
    pledge_list_lines = []
    with open("pledge.txt","r") as pledge:
        pledge_string = pledge.read()
        pledge_list = pledge_string.split()
    return pledge_list #(uncomment this)

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print(reverse_lookup_new(pledge_histogram, 1))
	print(reverse_lookup_new(pledge_histogram, 9))
	print(reverse_lookup_new(pledge_histogram, "Python"))
	# print(pledge_histogram)

if __name__ == '__main__':
    main()
