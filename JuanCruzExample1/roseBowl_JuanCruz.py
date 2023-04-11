''' Program for rose bowl winners'''

# -----------------------------
#
# Name: Juan Cruz
# Date: 04/07/2023
# Class: CS1300
#
# -----------------------------

# Time allows me to set a 5 second wait on a bad input
import time

# Workaround for filepaths to work from Lucas
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'Rosebowl.txt')


def main():
    '''Main program, allows user to choose what to do'''

    # Creative Element! A menu with error checking!

    # These first 4 lines tell the user to select a program to run
    print("Please choose a program:")
    print("1- All Rose Bowl winners.")
    print("2- Repeat Rose Bowl Winners with 4 or more wins.")
    print("3- Exit")

    # This sets a flag for the try exception handling
    userInput = False

    # This starts since the value of the flag is false
    while userInput is False:

        # This error checks the user input to make sure it is valid if it is
        # it sets the flag to true and breaks out of while loop
        try:
            choice = int(input("Enter a selection number: "))
            userInput = True

        # If the user input is invalid except runs and returns user to the input
        except ValueError:
            print("")
            print("ERROR!")
            print("You did not input a correct value.")
            print("Please enter a 1, 2 or 3.")

            # I added a delay so the user has time to read the error before trying again
            time.sleep(5)

    # These lines look at choice and run the correspending module
    if choice == 1:
        allWinners()
    if choice == 2:
        gameSorter()
    if choice == 3:
        print("Goodbye.")
        quit()

# This module takes all of the winners and shows them to the user, by printing only the keys
# in the dictionary


def allWinners():
    '''Lists all the winners'''

    # This starts a module that creates a list from the file
    listOfTeams = makeList()

    # This calls the module that makes the dictionary
    frequency = countList(listOfTeams)

    # This loop prints they key from the dictionary
    for keys, value in frequency.items():
        print(keys)

    # This sends the user back to main for another selection
    main()

# This module sorts the teams by wins


def gameSorter():
    '''Lists only teams that have won 4 or more times'''

    # This starts a module that creates a list from the file
    listOfTeams = makeList()

    # This calls the module that makes the dictionary
    frequency = countList(listOfTeams)

    # This line sorts the dictionary
    sortedByWins = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # This loop prints the sorted dictionary
    for i in sortedByWins:

        # This if only allows teams with 4 or more wins to be printed
        if i[1] >= 4:
            print(i[0], i[1])

    # This sends user back to main for another selection
    main()

# This module creates the list and returns it to the other modules


def makeList():
    '''Creates a list for use in othe rmodules'''
    listOfTeams = open(filename, 'r', encoding='utf8').read().splitlines()
    return listOfTeams

# This module creates the dictionary for the other modules


def countList(listOfTeams):
    '''Creates a dictionary for use in other modules'''
    # sets the dictionary to frequency variable
    frequency = {}

    # These two loops populate the value of the dictionary
    for team in listOfTeams:
        frequency[team] = 0
    for team in listOfTeams:
        frequency[team] = frequency[team] + 1

    # Returns the dictionary to the other modules
    return frequency


main()

# I found this very difficult at the start. I was trying to create a
# dictionary without having values  I did a lot of research before I
# finally gave up and tried it my way. I decided a list would be the
# best way to do this, so I created a list, then found a way to populate
# # the value section by wins. This allowed me to create the dictionary.
# After I did research on sorting dictionaries and was able  to complete
# the assignment. I decided I wanted the list and dictionary creation to
# use individual modules that way I could call them from the other modules
# without having a lot of repeated code.
