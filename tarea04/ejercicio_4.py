# Cree una función que reciba una secuencia de números separados por coma por parte del usuario e imprima una lista y una tupla que contengan dichos valores. El usuario debe ingresar un único input con los valores separados
# por comas.

def create_list_and_tuple_from_user_input():
    """
    Solicita al usuario ingresar una secuencia de números separados por coma y devuelve una lista y una tupla que contengan dichos valores.
    """
    num_list = []
    while True:
        numbers = input("Ingrese una secuencia de números separados por coma o escriba SALIR para salir: ")
        if numbers.lower() == "salir":
            break
        num_list.extend(numbers.split(","))
    num_tuple = tuple(num_list)
    return num_list, num_tuple

    #La función se llama así
    # my_list, my_tuple = create_list_and_tuple_from_user_input()
    # print(my_list)
    # print(my_tuple)

    #Y si finalmente el usuario escribe "SALIR", la función terminará y devolverá las últimas listas y tuplas que se crearon.


