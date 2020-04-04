# Take a string and change each letter for 
# its position in the english alphabet.

def alphabet_position(_lista):

    _lista = list(_lista)
    _outPut = []

    for i in range(len(_lista)):
        _lista[i] = cambio(_lista[i])

    for j in range(len(_lista)):
        if type(_lista[j]) == type(1):
            _outPut.append(_lista[j])

    return _outPut


def cambio(_campo):

    if _campo == "A" or _campo == "a":
        _campo = 1
    elif _campo == "B" or _campo == "b":
        _campo = 2
    elif _campo == "C" or _campo == "c":
        _campo = 3
    elif _campo == "D" or _campo == "d":
        _campo = 4
    elif _campo == "E" or _campo == "e":
        _campo = 5
    elif _campo == "F" or _campo == "f":
        _campo = 6
    elif _campo == "G" or _campo == "g":
        _campo = 7
    elif _campo == "H" or _campo == "h":
        _campo = 8
    elif _campo == "I" or _campo == "i":
        _campo = 9
    elif _campo == "J" or _campo == "j":
        _campo = 10
    elif _campo == "K" or _campo == "k":
        _campo = 11
    elif _campo == "L" or _campo == "l":
        _campo = 12
    elif _campo == "M" or _campo == "m":
        _campo = 13
    elif _campo == "N" or _campo == "n":
        _campo = 14
    elif _campo == "O" or _campo == "o":
        _campo = 15
    elif _campo == "P" or _campo == "p":
        _campo = 16
    elif _campo == "Q" or _campo == "q":
        _campo = 17
    elif _campo == "R" or _campo == "r":
        _campo = 18
    elif _campo == "S" or _campo == "s":
        _campo = 19
    elif _campo == "T" or _campo == "t":
        _campo = 20
    elif _campo == "U" or _campo == "u":
        _campo = 21
    elif _campo == "V" or _campo == "v":
        _campo = 22
    elif _campo == "W" or _campo == "w":
        _campo = 23
    elif _campo == "X" or _campo == "x":
        _campo = 24
    elif _campo == "Y" or _campo == "y":
        _campo = 25
    elif _campo == "Z" or _campo == "z":
        _campo = 26
    else:
        _campo = None

    return _campo

print(alphabet_position('Varela'))