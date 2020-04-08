# This time we want to write calculations using 
# functions and get the results. Let's have a look at 
# some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3


# Requirements:


# There must be a function for each number from 0 
# ("zero") to 9 ("nine")

# There must be a function for each of the following 
# mathematical operations: plus, minus, times, 
# dividedBy ( in Ruby and Python)divided_by

# Each calculation consist of exactly one operation 
# and two numbers

# The most outer function represents the left 
# operand, the most inner function represents the 
# right operand

# Divison should be integer division. For example, 
# this should return , not :22.666666...

# eight(divided_by(three()))


def zero(operation = None):
    if operation == None:
        return 0
    else:
        return int(eval("0" + operation))
def one(operation = None):
    if operation == None:
        return 1
    else:
        return int(eval("1" + operation))
def two(operation = None):
    if operation == None:
        return 2
    else:
        return int(eval("2" + operation))
def three(operation = None):
    if operation == None:
        return 3
    else:
        return int(eval("3" + operation))
def four(operation = None): 
    if operation == None:
        return 4
    else:
        return int(eval("4" + operation))
def five(operation = None): 
    if operation == None:
        return 5
    else:
        return int(eval("5" + operation))
def six(operation = None): 
    if operation == None:
        return 6
    else:
        return int(eval("6" + operation))
def seven(operation = None): 
    if operation == None:
        return 7
    else:
        return int(eval("7" + operation))
def eight(operation = None): 
    if operation == None:
        return 8
    else:
        return int(eval("8" + operation))
def nine(operation = None): 
    if operation == None:
        return 9
    else:
        return int(eval("9" + operation))

def plus(number): 
    return "+" + str(number)
def minus(number): 
    return "-" + str(number)
def times(number): 
    return "*" + str(number)
def divided_by(number): 
    return "/" + str(number)



print(four(plus(nine())))


#   eval()  --> eval is a built-in- function used in 
# python, eval function parses the expression 
# argument and evaluates it as a python expression. 
# In simple words, the eval function evaluates the 
# “String” like a python expression and returns the 
# result as an integer.