# Bob is preparing to pass IQ test. The most frequent task in this test is. 
# Bob observed that one number usually differs from the others in evenness. 
# Help Bob — to check his answers, he needs a program that among the given 
# numbers finds one that is different in evenness, and return a position of 
# this number.to find out which one of the given numbers differs from the others

# ! Keep in mind that your task is to help Bob solve a , which means indexes 
# of the elements start from real IQ test1 (not 0)


def iq_test(numbers):

    listOddEven = [int(i) % 2 for i in numbers.split() if i.isdigit()]

    return listOddEven.index(1 if listOddEven.count(0) > 1 else 0) + 1

print(iq_test("5 3 2"))