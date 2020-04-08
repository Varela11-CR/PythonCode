# Given a list of numbers, determine whether the sum 
# of its elements is odd or even.

# Give your answer as a string matching or 
# ."odd""even"

# If the input array is empty consider it as: 
# (array with a zero).[0]

# Example:
# odd_or_even([0])          ==  "even"
# odd_or_even([0, 1, 4])    ==  "odd"
# odd_or_even([0, -1, -5])  ==  "even"


def odd_or_even(arr):

    sum = 0

    for i in range(len(arr)):
        sum = sum + arr[i]

    if (sum % 2) == 0:
        return "even"
    else:
        return "odd"

print(odd_or_even([0, -1, -5]))