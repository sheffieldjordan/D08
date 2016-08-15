#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict() # estalishes an empty dictionary
    for key, val in dict_.items(): 
        val = d[key] # set the value of each key equal to 'val'
        if val not in inverse: # and check to see if 'val' is not in the inverse dictionary.
            inverse[val] = [key] # if it's not in the dictionary, then add it to the dictionary and set it's value to the key from the argument dictioanry
        else:
            inverse[val].append(key) # if 'val' is a key in the dictionary already, then add the argument-dictionary's key to the list-value for that key
    return inverse


def invert_dict_new(d):
    inverse = dict() # estalishes an empty dictionary
    for key, val in d.items():
        val = d[key] # set the value of each key equal to 'val'
        if val not in inverse: # and check to see if 'val' is not in the inverse dictionary.
            inverse[val] = [key] # if it's not in the dictionary, then add it to the dictionary and set it's value to the key from the argument dictioanry
        else:
            inverse[val].append(key) # if 'val' is a key in the dictionary already, then add the argument-dictionary's key to the list-value for that key
    return inverse


def print_hist_newest(d):
    for key, value in sorted(d.items()): # for each key and value in the inverted dictionary, return the sorted inverted dictionary as a list.
        print(key, value) # print each 'key', 'value' pair


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
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
