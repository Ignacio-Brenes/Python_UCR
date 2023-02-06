'''Suma'''
# Esta es una funcion para sumar los numeros ingresados por un usuario
# El resultado de la suma se guarda en el file "output_file_suma.txt"

def suma():
    '''Esta es la funcion para sumar'''
    # Crear lista vacia
    lista = []
    # Solicitar valores al usuario
    sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para finalizar):"))
    suma_numeros = 0
    while sumar !=0:
        # Agregar los valores ingresado la lista
        lista.append(sumar)
        sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para finalizar):"))
    print("Los numeros ingresados son: ")
    print(lista)
    for total in lista:
        suma_numeros += total
    print(f"El total de la suma de {lista} es:")
    print(suma_numeros)
    # Crear documento, escribir resultado y cerrar documento
    output_file = open("output_file_suma.txt", "a")
    output_file.write(f"La suma total de {lista} es: {suma_numeros}\n")
    output_file.close()
