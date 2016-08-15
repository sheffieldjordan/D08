#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
# def print_hist_old(h):
#     for key, value in sorted(h.items()):
#         return h


def print_hist_new(h):
	for key, value in sorted(h.items()):
		print(key, value)
	# print(sorted(h))


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
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    # print(histogram_new(get_pledge_list()))
    print(print_hist_new(histogram_new(get_pledge_list())))

if __name__ == '__main__':
    main()
