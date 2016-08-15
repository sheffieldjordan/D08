#!/usr/bin/env python3
# Imports
import random


# Body
def printRoster(bootcampParticipants):
    """ prints entire roster """
    for x in bootcampParticipants:
        print(x)


def getRandomParticipantIndex(roster):
    """ Returns random index of person in roster """
    for idx, name in enumerate(roster):
        print("{}: {}".format(idx, name))
    return random.randint(0, len(roster) - 1)


def getPerson(roster):

    #""" Returns person (string) from roster """
    idx = input("Person's Index: ")
    name = roster[int(idx)]
    return name
    # rewrite getPerson() to take a index and roster; return name at index
    # pass


def addPerson(name, roster):
    roster.append(name)
    """ Adds person (string) to roster """
    # rewrite addStudent() to take a name and roster; add name to roster
    # pass


def get_excuse():
    excuses = ["My dog ate my homework",
               "I drank too much beer last night.",
               "\"Bored to Death\" marathon",
               "Laptop went up in flames",
               "Ain't nobody got time for that!",
               "My plane got stuck in Vegas",
               "I was watching \"The Big Lebowski\"",
               "Wait, I was supposed to do something?"]

    return excuses[random.randint(0, len(excuses) - 1)]


###############################################################################
def main():
    """ Main -- prints the bootcamp roster, adds Daniel, and then prints
    excuses """
    bootcampParticipants = ["Malavika", "Edward", "Nancy", "Ankeet", "Anna",
                            "Arnav", "Sandeep", "Shannon", "Natalia", "Nia",
                            "Nicolas", "Nihar", "Suchismita", "Vikram", "Yifei",
                            "Avi", "Nisha", "Peter", "Priyanka", "Rohit",
                            "Sophie", "Selenne", "Carina", "Lucia", "Meghana",
                            "Harman", "Robin", "Karan", "Liz", "Shazeda",
                            "Jolly", "Michelle", "Morgan", "Mudit"]

    printRoster(bootcampParticipants)# your one line of code goes here to print roster #

    addPerson('Daniel', bootcampParticipants)#add 'Daniel' to bootcampParticipants

    # Your Code Here ###
    getRandomParticipantIndex(bootcampParticipants) # get random participant

    name = getPerson(bootcampParticipants)# print person's name who has excuse today.

    #
    # print person's name who has excuse today.
    # Fix code below to print name and excuse of person:
    print("{} said: {}".format(name, get_excuse()))


if __name__ == "__main__":
    print("Excuse Generator: ") 
    main()
