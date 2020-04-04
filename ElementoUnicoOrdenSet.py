# It takes the given item and makes it a list, then deletes 
# the repeating items and sorts them.

def unique_in_order(iterable):

    iterable = list(iterable)
    newIterable = sorted(set(iterable))
    
    #   set     --> es un conjunto de elementos el cual no mantiene elementos repetidos
    #   sorted  --> es una funcion para ordenar los elementos

    #   newIterable = set(set(iterable))    --> esta linea tambien ordena los elementos,
    #                                           pero los devuelve como un conjunto.

    return newIterable


print(unique_in_order("ABBCcAD"))