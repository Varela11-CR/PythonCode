# It takes a list with names, if the name has 4 digits 
# it is friend and a new list is added which is returned.

def friend(x):
    #Code

    friends = []
    xLength = len(x)

    for i in range(xLength):
        if len(x[i]) == 4:
            friends.append(x[i])

    print(friends)
    return friends


x = ["Ryan", "Kieran", "Jason", "Yous"]
friend(x)