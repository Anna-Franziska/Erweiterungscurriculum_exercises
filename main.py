


def remove_duplicates(lst):
    dupli = set(lst)
    for x in lst:
        return dupli

# I tried out the function number 4
practice = [3, 44, 5, 6, 44]
# print(remove_duplicates(practice))



def list_func(numbers, integer):
   for i in range(len(numbers)):
     if  numbers[i] == integer:
          numbers[i] = 6
   print(numbers[::-1])
   return numbers

#trying out code again
cucumber = [4, 5, 5, 7, 5]
print(list_func(cucumber, 5))

