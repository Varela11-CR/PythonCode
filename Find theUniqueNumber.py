# There is an array with some numbers. All numbers are 
# equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

from functools import lru_cache

def find_uniq(arr):

    for i in range(len(arr)):
        x = arr.count(arr[i])
        if x == 1:
            n = arr[i]
            return n


print(find_uniq([ 0, 0, 0.55, 0, 0 ]))


def find_uniq_optimized(arr):

    e = set(arr)

    for i in e:
        if arr.count(i) == 1:
            return i

print(find_uniq_optimized([ 0, 0, 0.55, 0, 0 ]))