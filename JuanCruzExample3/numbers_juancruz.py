''' Program for sorting numbers'''

# -----------------------------
#
# Name: Juan Cruz
# Date: 03/24/2023
# Class: CS1300
#
# -----------------------------


# Workaround for filepaths to work from Lucas
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'Numbers.txt')


def main():
    '''Main function that prints the results to the user'''

    # Calls the displaynumbers function to find out how many numbers in file then prints result
    amount = displayNumbers("Numbers.txt")
    print("There are", amount, "numbers in the Numbers.txt file")

    # Calls displayMax function to find the largest number in file then prints result
    maxNumber = displayMax("Numbers.txt")
    print("The biggest number in the file is", maxNumber, ".")

    # Calls displayMin function to find the smallest number in file then prints result
    minNumber = displayMin("Numbers.txt")
    print("The smallest number in the file is", minNumber, ".")

    # Creative element, calls sumNumbers function to add all the numbers together, and prints result
    totalSum = sumNumbers("Numbers.txt")
    print("The total of all the numbers in the file is", totalSum, ".")


def displayNumbers(numberFile):
    ''' This module counts all the entries in the file and returns the amount'''

    # Open File
    numberFile = open(filename, 'r', encoding="utf8")
    count = 0

    # This loop counts the numbers in the file
    for line in numberFile:
        count += 1

    # Closes File
    numberFile.close()

    # Returns count
    return count


def displayMax(maxNumberFile):
    '''This module processes the file and returns the maximum number'''

    # Opens file
    maxNumberFile = open(filename, 'r', encoding="utf8")
    maxNum = int(maxNumberFile.readline())

    # This loop finds the largest number in the file
    for line in maxNumberFile:
        num = int(line)
        if num > maxNum:
            maxNum = num

    # Closes file
    maxNumberFile.close()

    # Returns the largest number
    return maxNum


def displayMin(minNumberFile):
    '''This module processes the file and finds the minimum number'''

    # Opens file
    minNumberFile = open(filename, 'r', encoding="utf8")
    minNum = int(minNumberFile.readline())

    # Finds smallest number in the file
    for line in minNumberFile:
        num = int(line)
        if num < minNum:
            minNum = num

    # Closes file
    minNumberFile.close()

    # Returns the smallest number
    return minNum

# Creative element, this adds all the numbers in the file together


def sumNumbers(sumNumberFile):
    '''This module adds all the numbers in the file together and returns the sum'''

    # Opens file
    sumNumberFile = open(filename, 'r', encoding="utf8")
    sumNum = 0
    filename.rstrip()

    # Loop adds each number together one at a time
    for line in sumNumberFile:
        for number in line:
            if number.isdigit() is True:
                sumNum = sumNum + int(number)

    # Closes File
    sumNumberFile.close()

    # Returns the sum
    return sumNum


main()

# I used the provided solutions to this program because I found them clean
# and easy to understand and modify. I added a sum funtion to demonstrate
# that I understood how it was working. I also adapted Lucas' OS import
# and filename structure for simplification.
