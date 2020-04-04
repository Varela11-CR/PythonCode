# Take the item and make it a list, then prevent an item 
# from being repeated next.

def unique_in_order(iterable):

    iterable = list(iterable)
    newIterable = []

    if iterable:
        newIterable.append(iterable[0])

    for i in range(1,len(iterable)):
        if iterable[i] != iterable[(i - 1)]:
            newIterable.append(iterable[i])

    return newIterable

print(unique_in_order([1,2,2,3,3]))
