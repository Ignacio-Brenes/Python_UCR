#Escriba una función que elimine todas las apariciones de un elemento en una lista. Tanto la lista como el valor que se quiere eliminar deben ser parámetros de la función.

def remove_elements_from_list(lst, value):
    """
    Elimina todas las apariciones del valor dado de una lista.
    """
    while value in lst:
        lst.remove(value)
    return lst

# La función recibe dos parámetros: la lista en la que se quiere eliminar elementos y el valor que se desea eliminar de la lista. 
# Luego, utiliza un ciclo while para eliminar todas las apariciones del valor dado hasta que ya no queden más en la lista. 
# Finalmente, devuelve la lista modificada.