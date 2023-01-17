'''
Anderson Iskowitz
Unit 6 Assignment
1/11/23
'''
import random

def get_birthdays():
    class_birth = []
    for x in range(23):
        class_birth.append(random.randint(1, 365))
    print(class_birth)
    return class_birth
def is_duplicate(lists):
    for x in range(22):
        for y in range(x + 1, 23):
            if lists[x] == lists[y]:
                return True
    return False
def main():
    while True:
        print("Welcome! This program will calculate how many classes have two students with the same birthday")
        play = input("Would you like to play?: ")
        if play in ["y", "Y", "yes", "Yes"]:
            counter = 0
            while True:
                try:
                    y = int(input("How many times would you like to run the simulation? "))
                except ValueError:
                    print("Sorry, I didn't understand your entry. Please enter a positive integer.")
                    continue
                else:
                    break
            for x in range(y):
                z = get_birthdays()
                if is_duplicate(z) is True:
                    counter = counter + 1
                else:
                    counter = counter
            percent = int((counter/y) * 100)
            print("the percent of times there was a duplicate was", percent, "%.")
            break
        if play in ["n", "N", "No", "no"]:
            print("Ok! Goodbye")
            break
        pass


main()
