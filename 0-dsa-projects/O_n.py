def sum_list(numbers):
    total = 0
    
    for num in numbers:
        total += num
        
    return total


# we iterate through each variable making this constant based on our data 


def find_letter(data, target):
    for letter in data:
        if letter == target:
            return True
    return False

# Example usage:

letters = ["a", "b", "c", "d", "e", "f", "g"]

print(find_letter(letters, "d"))
# Why This Is Still O(n)

# At first glance someone might think:

# "It stops when it finds d, so it only loops a few times."

# But Big-O looks at the worst case, not the best case.

# Possible scenarios:

# Case	What Happens	Complexity
# Best Case	Target is first element	O(1)
# Middle Case	Target somewhere inside	O(n/2)
# Worst Case	Target is last element or not present	O(n)

# Even if the target is in the middle, that is:

# n / 2

# But in Big-O:

# O(n/2) → O(n)

# because constants are dropped.


buffer = bytearray(6)

print(buffer)

# This literally creates 6 bytes in memory.