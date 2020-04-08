# Given an array of ones and zeroes, convert the equivalent 
# binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary 
# representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11

# However, the arrays can have varying lengths, not just 
# limited to 4.


def binary_array_to_number(arr):

    number = 0
    count = len(arr) - 1
    exp = 0

    while(count >= 0):
        if arr[count] != 0:
            number = number + (2 ** exp)
        
        count -= 1
        exp += 1
    
    return number


print(binary_array_to_number([1,1,1,1]))