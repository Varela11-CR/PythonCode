# Consider an array/list of sheep where some sheep may be 
# missing from their place. We need a function that counts 
# the number of sheep present in the array (true means 
# present).


def count_sheeps(sheep):

    count = 0

    for i in range(len(sheep)):
        if sheep[i]:
            count += 1

    return count


sheeps = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]

print(count_sheeps(sheeps))
