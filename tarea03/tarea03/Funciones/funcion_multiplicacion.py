# # # PROGRAMA PARA MULTIPLICACION DE 2 O MAS NúMEROS

# total = 1
# while True:
#   number = float(input("Ingresa un número y seguiré multiplicando hasta que ingreses 1 para SALIR: \n"))
#   if number == 1:
#     print(f"El total de la multiplicación es: {total}")
#     break
#   else:
#     total *= number


# Nuevo Codigo, con validacion del valor ingresado.
# Output a un file
'''Multiplicacion'''

# Esta es una funcion para sumar los numeros ingresados por un usuario


# El resultado de la mulitplicacion se guarda en el file "output_file_multiplicacion.txt"


def multiplicacion():
    '''Esta es la funcion para multiplicar'''
    total = 1
    while True:
        try:
            # El usuario debe ingresar la cantidad de numeros que desee
            number = int(input("Ingresa un número y seguiré multiplicando hasta que ingreses 0 para SALIR: \n"))
        # Verificacion del input del usuario
        except ValueError:
            print("Ingrese un numero! Trate nuevamente.")
            continue
        # Si el usuario ingresa el numero cero se termina el programa
        if number == 0:
            print(f"El total de la multiplicación es: {round(total)}")
            break
        else:
            total *= number
    # Abre/Crea un documento en modo "append"
    output_file = open("output_file_multiplicacion.txt", "a")
    # Agrega el resultado al documento existente
    output_file.write(f"El total de multiplicacion es: {total}\n")
    # Cierra el documento
    output_file.close()

