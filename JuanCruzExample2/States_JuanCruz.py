''' Program for states and capitals'''

# -----------------------------
#
# Name: Juan Cruz
# Date: 04/04/2023
# Class: CS1300
#
# -----------------------------

# Workaround for filepaths to work from Lucas
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'StatesANC.txt')


def main():
    '''Main program, allows user to choose what to do'''

    # Creative Element! A menu!

    # These first 4 lines tell the user to select a program to run
    print("Please choose a program:")
    print("1- States and capitals that start with the same letter.")
    print("2- User enters a state and gets information about it.")
    print("3- Exit")

    # This takes the users input and saves it in choice variable
    choice = input("Enter a selection number: ")

    # These next few lines are all error checks to make sure the
    # user only entered a 1, 2 or 3.
    while choice.isalpha() or choice == "":
        choice = input("Error, Please enter 1, 2 or 3: ")
    choice = int(choice)
    while choice < 1 or choice > 3:
        choice = input("Please enter 1, 2 or 3: ")

    # These lines look at choice and run the correspending module
    if choice == 1:
        statePrint()
    if choice == 2:
        findState()
    if choice == 3:
        print("Goodbye.")
        quit()


def statePrint():
    '''Module to print matching states'''

    # This opens the file
    stateFile = open(filename, 'r', encoding="utf8")

    # This goes line by line checking to see if the first
    # word in the line's, first letter matches the first
    # letter of the 4th word. If it does it prints it
    for line in stateFile:
        data = line.split(",")
        if data[0][0:1] == data[3][0:1]:
            print(data[0] + ", " + data[3])

    # Closing the file
    stateFile.close()

    # This returns us to the main menu to allow further selections
    main()


def findState():
    '''Find state in file and return data'''

    # This line takes the user input and saves it as state variable
    state = input("Enter the name of a state: ")

    # Error checking, it forces the input to a title case
    state = state.title()

    # This opens the text file containing the state data
    infile = open(filename, 'r', encoding="utf8")

    # This variable is used in the while loop to see if the
    # information was located
    found = False

    # This saves each line read in the file to state_data variable
    # so we can compare
    state_data = infile.readline()

    # This loop performs the work. if found is false and the entry is not blank
    # it runs
    while (found is False) and (state_data != ""):
        data = state_data.split(",")

        # If the input from the user matches the first word in a line it prints
        # the lines below.
        if data[0] == state:
            print("Abbreviation:", data[1])
            print("Nickname:", data[2])
            print("Capital:", data[3].rstrip())
            found = True

        # This moves to each additional line checking
        state_data = infile.readline()

    # Error check. If there is no match, this runs the error module
    while (found is False):
        error()

    # closing the file
    infile.close()

    # returns user to main menu to allow for additional states to be checked.
    main()


def error():
    '''Error Module'''

    # This warns the user an error has been detected
    print("Error! Enter a name of a state!")

    # this returns to the findState module to allow new input
    findState()


main()

# This code took me several hours to figure out. I tried using lists to detect
# words but was not having any success. I modified the provided 'answer' code then turned
# to error checking to ensure good inputs.
