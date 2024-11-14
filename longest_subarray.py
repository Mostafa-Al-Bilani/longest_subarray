"""a function that takes a binary list and gives back the length of a list with equal 0 and 1's."""
array = [0, 1, 1, 0, 0, 1, 0 , 0, 1, 1 ,1 ,1 ,1]

def longest_subarray(array):
    length = len(array)
    count0 = 0
    count1 = 0
    for i in range(length):
        if array[i] == 1:
            count1 += 1
        if array[i] == 0:
            count0 += 1
#after checking how many 0 and 1's there is the we take the value of the least
    if count0 < count1:
        return count0
    return count1
print(longest_subarray(array))
