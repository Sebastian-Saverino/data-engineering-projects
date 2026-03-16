
array = [1,2,3,7,4,9,10,5,8,9]

# if(arr[j] > arr[j+1]) and the swap should be swap(j, j+1)

# for i in array:
#     len[array]


# for i in array:
#     for j in array - 1:
#         array[j <]


# Actual Bubble Sort


for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)




# Need to practice this more.


