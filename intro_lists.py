
def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    list_one[0], list_one[1], list_one[2] = list_one[2], list_one[1], list_one[0]
    return print(list_one)

def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    list_one = list_one[1:] + list_one[:1]
    return print(list_one)
def max_end(list_one):
    """
    This function will find if the first or last element of a list is larger, then set all the elements
    of a list to be greater value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    list_one.sort()
    print(list_one)
    g = list_one[-1]
    new_list = [g,g,g]
    return print(new_list)

def main():
    swap([1, 2, 3])
    rotate_left([1, 2, 3])
    max_end([5, 6, 7])

main()