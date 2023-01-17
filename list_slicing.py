def main():
    # The list below will be used for all of the exercises below:
    names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen”",
    "Jackie", "Kurt", "Linda"]

    # Example: print the first three names from the list
    # Answer print(names[0:3])

    # 1. Print ['Doug', 'Emma']

    print(names[3:5])

    # 2. Print [‘Brenda’, ‘Chad’, ‘Doug’, ‘Emma’, ‘Francis’]

    print(names[1:6])

    # 3. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using two numbers in the slice)

    print(names[5:15])
    # 4. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using one number in the slice)

    print(names[5:])

    # 5. [‘Linda’] (using a positive number)
    print(names[11])

    # 6. [‘Linda’] (using a negative number)

    print(names[-1])

    # 7. [‘Brenda’, ‘Doug’, ‘Francis’, ‘Harold’]

    print(names[1:8:2])

    # 8. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’]

    print(names[0:11:2])

    # 9. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’] (using a different way than above.
    # HINT: If you leave a slice number blank, the default is either the beginning or the end of the list,
    # depending on which side of the colon is blank.
    print(names[:11:2])

    # 10. [‘Linda’, ‘Kurt’, ‘Jackie’]

    print(names[11:8:-1])
    # 11. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']

    print(names[-1:0:-1])

    # 12. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']
    # (in a different way than 11. See hint for 9 for help.)

    print(names[11:0:-1])



if __name__ == '__main__':
    main()