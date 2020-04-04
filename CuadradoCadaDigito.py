# Take the number and make it a list, then show each item 
# squared.

def square_digits(num):

    num = [int(i) for i in str(num)]

    for i in range(len(num)):
        num[i] = num[i] ** 2

    num = [str(i) for i in num]
    num = "".join(num)
    num = int(num)

    return num


num = 9119

print(square_digits(num))


