def count_integer(numbers, integer):
    counter = 0
    for i in numbers:  # use of the for loop to iterate over the list
        if i == integer:
            counter += 1  # += allows the loop to move on by 1 increment
    if counter == 0:  # Code specifies that if the integer doesn't exist it should return -1
        counter = -1
        return counter


def compare_lists(list1, list2):
    common_list = list()  # ensures a common list

    longer_list = list1 if len(list1) >= len(list2) else list2  # the elements of the lists are compared
    shorter_list = list2 if len(list1) >= len(list2) else list1

    return ([
        element for element in shorter_list if element in longer_list
        # making sure elements found in both lists are added to new list
    ])


def count_vowels(text):
    if type(text) == str:  # if the data type is a string it counts the vowels
        return len([letter for letter in text.lower() if letter in ["a", "e", "i", "o",
                                                                    "u"]])  # counts the vowels using len after specifing which letters are vowels
    else:
        return -1  # if the data type is not a string it returns -1


def hamming(text1, text2):
    if len(text1) <= len(text2):
        h = len(text2) - len(text1)  # = 0 if len(text1) == len(text2)
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                h += 1

    else:
        assert len(text1) > len(text2) #assert ensures that the file cannot be different than specified
        h = len(text1) - len(text2)
        for i in range(len(text2)):
            if text1[i] != text2[i]:
                h += 1
    return h


def transform_to_row(infile, outfile):
    with open(infile, "r") as reader:  # with open ensures you don't have to close the file
        i = reader.readlines()  # first opened in reader format to "read" the text
        for line in i:
            i = line.split(",")  # line ist split by a ","

    with open(outfile, "w") as writer:  # new file is created in writing mode
        for line in i:
            writer.write(
                line + "\n")  # the previously read files are written into the outfile with a break after each line


def remove_duplicates(lst):
    set_of_list = list(
        set(lst))  # making sure argument will become a list + using built in function set to remove duplicates
    if len(lst) == len(
            set_of_list):  # len returns the number of items in the object, returns list as is if no duplicates found
        print("No duplicates found in list")  # additionally prints statement

    return set_of_list

# practise list = my_list = [1,1,2,2,3,3,4,5]
