#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports


# Body


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
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
