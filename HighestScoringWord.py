# Given a string of words, you need to find the highest scoring 
# word.

# Each letter of a word scores points according to its position 
# in the alphabet: etc.a = 1, b = 2, c = 3

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears 
# earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):
    
    listWords = x.split(" ")
    valueWords = []
    higher = 0

    for i in range(len(listWords)):

        value = 0

        for j in listWords[i]:

            value = numberWord(j) + value
        
        valueWords.append(value)

    for i in range(len(valueWords)):

        if int(valueWords[i]) > higher:
            higher = valueWords[i]
            index = i
        elif valueWords[i] == higher:
            pass

    return listWords[index]

def numberWord(letter):

    if letter == "a":
        letter = 1
    elif letter == "b":
        letter = 2
    elif letter == "c":
        letter = 3
    elif letter == "d":
        letter = 4
    elif letter == "e":
        letter = 5
    elif letter == "f":
        letter = 6
    elif letter == "g":
        letter = 7
    elif letter == "h":
        letter = 8
    elif letter == "i":
        letter = 9
    elif letter == "j":
        letter = 10
    elif letter == "k":
        letter = 11
    elif letter == "l":
        letter = 12
    elif letter == "m":
        letter = 13
    elif letter == "n":
        letter = 14
    elif letter == "o":
        letter = 15
    elif letter == "p":
        letter = 16
    elif letter == "q":
        letter = 17
    elif letter == "r":
        letter = 18
    elif letter == "s":
        letter = 19
    elif letter == "t":
        letter = 20
    elif letter == "u":
        letter = 21
    elif letter == "v":
        letter = 22
    elif letter == "w":
        letter = 23
    elif letter == "x":
        letter = 24
    elif letter == "y":
        letter = 25
    elif letter == "z":
        letter = 26
    
    return letter


print(high('take me to semynak'))