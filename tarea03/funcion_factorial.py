'''Factorial'''
# Esta es una funcion para obtner el factorial de un numero ingresado por un usuario
# El resultado de la suma se guarda en el file "output_file_factorial.txt"

def factorial():
    '''Funcion para Restar'''
    while True:
        num_usuario = int(input("Ingrese un numero positivo entero al que se le va a \
calcular el factorial: "))
        numero_factorial = 1
        if num_usuario < 0:
            print("---> Se necesita un numero positivo entero (Mayor o igual a ZERO), \
ejecute el codigo nuevamente y ingrese un numero <---")
        elif num_usuario == 0 or num_usuario == 1:
            print("El factorial de ", num_usuario," es", numero_factorial)
        else:
            for i in range(1, num_usuario+1):
                numero_factorial = numero_factorial*i
            print ("El factorial del número",num_usuario,"es",numero_factorial)
            # Open/create output file in append mode
            output_file = open("output_file_factorial.txt", "a")
            # Appends the results to an output file
            output_file.write(f"El factorial de {num_usuario} es: {numero_factorial}\n")
            output_file.close() # Closes the file

# Preguntar al usuario si desea continuar
        continuar = str(input("Indique (Y/N) para ingresar un nuevo numero: "))
        continuar = continuar.upper()
        if continuar == "N":
            print("Gracias!!!")
            break
        else:
            continue
