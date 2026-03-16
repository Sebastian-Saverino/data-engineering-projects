import math

data = [True,True,True,True,True,True,False,False,False,False]

jump_amount = int(math.sqrt(len(data)))

while jump_amount == True:
    data[jump_amount]
    if data[jump_amount] == False:
        False
        for i in data:
            print(i)







index = 0

# Jump phase
while index < len(data) and data[index] == True:
    index += jump_amount

# Linear search phase
start = index - jump_amount

for i in range(start, min(index + 1, len(data))):
    if data[i] == False:
        print("First False at index:", i)
        break