# You have an array of numbers.
# Your task is to sort ascending odd numbers but even 
# numbers must be on their places.

# Zero isn't an odd number and you don't need to move 
# it. If you have an empty array, you need to return 
# it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def sort_array(source_array):

    oddIndex = [i for i in range(len(source_array)) if (source_array[i] % 2) != 0]

    for i in range(len(source_array)):

        if (source_array[i] % 2) != 0:

            for j in oddIndex:

                if source_array[i] > source_array[j]:
                    aux = source_array[i]
                    source_array[i] = source_array[j]
                    source_array[j] = aux

            oddIndex.pop(0)
        
    return source_array
    
    


print(sort_array([5, 3, 2, 8, 1, 4]))