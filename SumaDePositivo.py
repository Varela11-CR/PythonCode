# Take a list with numbers, show only the sum of the 
# positive numbers, using a for loop to make a new 
# list with the positive numbers, and use another 
# loop to make the sum of the positive numbers.

def positive_sum(arr):
    # Your code here

    arrLength = len(arr)
    suma = []
    total = 0

    for i in range(arrLength):
        if arr[i] > 0:
            suma.append(arr[i])

    sumaLength = len(suma)

    for i in range(sumaLength):
        total = total + suma[i]

    return total


arr = [-1,-2,-3,-4,-5]
print(positive_sum(arr))