# Exercise 1
def power(a, b):
   if a < 0 or b < 0:
       return -1
   if a == 1:
       return 1
   if b > 0:
        return a * power(a, b - 1)
   else:
        return 1


# Exercise 2

def binary_search(numbers, num):
    assert num in numbers
    numbers = sorted(numbers) #make sure the list is sorted
    return _binary_search(numbers, num, 0, len(numbers)-1)


def _binary_search(numbers, num, start, end):

    middle_index = int((start + end) / 2)
    curr_number = numbers[middle_index]

    if curr_number == num: # In case the first middle index is desired value
        return middle_index

    elif num < curr_number:
        # go left
        new_start = start
        new_end   = middle_index  # - 1
        return _binary_search(numbers, num, new_start, new_end)

    else:  # num > curr_number
        # go right
        new_start = middle_index  # + 1
        new_end   = end
        return _binary_search(numbers, num, new_start, new_end)

#Exercise 3 - 7
class HashTable:

    def __init__(self, size):

        self.size = size

        self.buckets = [[] for i in range(size)]

    def __my_hash(self, element):

        if type(element) == int or type(element) == float:
            return element % self.size

        return len(element) % self.size

    def insert(self, element):

        h = self.__my_hash(element)

        self.buckets[h].append(element)

    def get_element(self, element):

        bucket = self.__my_hash(element)

        if element in self.buckets[bucket]:
            self.buckets[bucket].remove(element)

            return element

        return False

    def get_size(self):

        return len(self.size)























