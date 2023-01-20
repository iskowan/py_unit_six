"""
Anderson Iskowitz
Unit 6 Assignment
1/11/23
"""

import random                       # importing random to get random int
import time                         # importing time for pausing time
import sys                          # importing sys for scrollTxt


class Color:                                                                                                                # defining a class for text
    purple = '\033[95m'
    cyan = '\033[96m'
    dark_cyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


def scroll_txt(text):                                                                                                       # https://replit.com/talk/ask/How-do-we-print-letters-by-letters-in-python/34360
    for char in text:                                                                                                       # for the amount of characters, type the text
        sys.stdout.write(char)                                                                                              # write the character
        sys.stdout.flush()                                                                                                  # buffers the code
        time.sleep(0.03)                                                                                                    # pause for .03 seconds


def intro():
    '''
    :return: returns the amount of times that the user wants to run the code
    '''
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]                                            # defining a list called animation
    for i in range(20):                                                                                                     # loop this 20 times
        time.sleep(0.3)                                                                                                     # pause time
        sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])                                                  # write waiting and animation
        sys.stdout.flush()
    time.sleep(.5)                                                                                                          # pauses code for .5 seconds
    print("\rFinished")                                                                                                     # replace previous text with this
    scroll_txt("Welcome! This program will calculate how many classes have two students with the same birthday\n")          # intro
    while True:
        scroll_txt("Would you like to play?:")                                                                              # asking user if they would like to play
        play = input(" ")                                                                                                   # getting input
        if play in ["y", "Y", "yes", "Yes"]:                                                                                # if the input is one of these
            while True:
                try:                                                                                                        # do this
                    scroll_txt("How many times would you like to run the simulation?:")                                     # ask user how many times they would like to run the simulation
                    y = int(input(" "))                                                                                     # getting input
                    return y                                                                                                # return value y
                except ValueError:                                                                                          # when the output is an error do this
                    scroll_txt("Sorry, I didn't understand your entry. \nPlease enter a positive integer.\n")               # print the following
                    time.sleep(1)                                                                                           # pause code for 1 second
                    continue                                                                                                # continue code
        if play in ["n", "N", "No", "no"]:                                                                                  # if input is
            scroll_txt("Ok! Goodbye.")                                                                                      # print this
            quit()                                                                                                          # end code


def get_birthdays():
    '''
    :return: returns the list made
    '''
    class_birth = []                                                                                                        # creates a list
    for x in range(23):                                                                                                     # loops 23 times
        class_birth.append(random.randint(1, 365))                                                                          # get random int and add it to the list
    return class_birth                                                                                                      # return the list


def is_duplicate(lists):
    '''
    :param lists: lists will be a list that you want to check for duplicate
    :return: returns True or False depending on if there was a duplicate or not
    '''
    for x in range(22):                                                                                                     # loops 22 times
        for y in range(x + 1, 23):                                                                                          # adds 1 to x and loops 23 times
            if lists[x] == lists[y]:                                                                                        # compares list to itself
                return True                                                                                                 # if there was a duplicate returns true
    return False                                                                                                            # if there was not a duplicate, return false


def main():
    y = intro()                                                                                                             # calls intro
    counter = 0                                                                                                             # sets counter as 0
    for x in range(y):                                                                                                      # loops for as many times as the user said in intro
        z = get_birthdays()                                                                                                 # call birthdays
        if is_duplicate(z) is True:                                                                                         # if is_duplicates returns true
            counter += 1                                                                                                    # add one to counter
        else:                                                                                                               # if is_duplicates returns anything else (False)
            counter = counter                                                                                               # counter is the same
    percent = int((counter/y) * 100)                                                                                        # calculate percent
    scroll_txt("The percent of duplicates found was " + Color.bold + str(percent) + "%." + Color.end)                       # print the result to the user
    scroll_txt("\nWould you like to play the simulation again?: ")                                                          # asks user if they would like to play again
    while True:
        t = input(" ")                                                                                                      # gets input
        if t in ["y", "Y", "Yes", "yes"]:                                                                                   # if input is one of the items in a list
            main()                                                                                                          # call main
        if t in ["n", "N", "no", "No"]:                                                                                     # if input is one of the items in the list
            quit()                                                                                                          # quit code
        else:
            scroll_txt("Sorry I didn't get that, please type yes or no: ")                                                  # print this
            continue                                                                                                        # continue code

main()                                                                                                                      # calling main function
