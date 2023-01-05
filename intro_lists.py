'''
names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen", "Jackie", "Kurt", "Linda"]
print(names[3:5])
print(names[1:6])
print(names[5:15])
print(names[5:])
print(names[11])
print(names[-1])
print(names[1:8:2])
print(names [0:11:2])
print(names[:11:2])
print(names[11:8:-1])
print(names[-1:0:-1])
print(names[11:0:-1])
'''

def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    pass # make sure to remove this line before beginning work on this function
    del list_one

def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    pass # make sure to remove this line before beginning work on this function


def max_end(list_one):
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    pass # make sure to remove this line before beginning work on this function

def main():
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    swap(list_one)