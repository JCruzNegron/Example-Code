''' Program for program that accepts a word as input and determines whether
or not it has three consecutive letters that are consecutive letters in the alphabet'''

# -----------------------------
#
# Name: Juan Cruz
# Date: 03/13/2023
# Class: CS1300
#
# -----------------------------


def main():
    '''This is the main program, it takes user input, then the return from
      isTripleConsecutive produce an answer'''
    word = input("Please enter a word to check: ")

    # Forces word into lowercase, since uppercase characters have
    # different ord values than lowercase
    word = word.lower()

    #This creative element checks to make sure numbers or special characters are not used
    while not word.isalpha():
        print("Error, please enter a word without numbers or special characters.")
        word = input("Please enter a word to check: ")

    #This section calls the isTripleConsecutive function, then provides the answer
    if isTripleConsecutive(word):
        print("The word",word, "contains three consecutive letters in the alphabet.")
    else:
        print("The word",word, "does not contain three consecutive letters in the alphabet.")
        print("Try a word like thirsty, nope, afghanistan, or student.")


# The function that does the work
def isTripleConsecutive(word):
    '''This uses the ord function to turn the letters into numbers, then compare
      the numbers to see if they are consecutive'''

    # This loop checks the ord values to the characters right beside them, and if
    # three are consecutive, it returns true
    for i in range(len(word)-2):
        if ord(word[i])+1 == ord(word[i+1]) and ord(word[i+1])+1 == ord(word[i+2]):
            return True

    # If the program does not find consecutive values, it returns false
    return False


main()


# I had to cheat a little bit on this one to figure out how to do it
# I was going to make a list of letters and compare it that way
# but I ended up doing research and finding using ord was the
# best way to do it. the formula was acquired from the internet
# but I understand how it works now that i've played with it.
