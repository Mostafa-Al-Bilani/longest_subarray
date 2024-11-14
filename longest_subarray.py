array = [0, 1, 1, 0, 0, 1, 0 , 0, 1, 1 ,1 ,1 ,1]

def longest_subarray(array):
    Length = len(array)
    count0 = 0
    count1 = 0
    for i in range(Length):
        if array[i] == 1:
            count1 += 1
        if array[i] == 0:
            count0 += 1
    if count0 < count1:
        return count0
    else:
        return count1
print(longest_subarray(array))
