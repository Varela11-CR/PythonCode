# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

# for example, a tower of 3 floors looks like below

# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]
# and a tower of 6 floors looks like below

# [
#   '     *     ', 
#   '    ***    ', 
#   '   *****   ', 
#   '  *******  ', 
#   ' ********* ', 
#   '***********'
# ]


def tower_builder(n_floors):

    spaces = " " * (n_floors - 1)
    asteriks = "*"
    tower = []

    for i in range(n_floors):
        tower.append(spaces + asteriks +spaces)
        spaces = " " * (n_floors - (i + 2))
        asteriks = asteriks + ("*" * 2)

    return tower



print(tower_builder(3))