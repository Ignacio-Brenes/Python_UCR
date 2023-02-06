'''Factorial'''
# Esta es una funcion para obtner el factorial de un numero ingresado por un usuario
# El resultado de la suma se guarda en el file "output_file_factorial.txt"

def factorial():
    '''Funcion para Restar'''
    while True:
        # Recibir numero del usuario y almacenarlo
        num_usuario = int(input("Ingrese un numero positivo entero al que se le va a calcular el factorial: "))
        numero_factorial = 1
        # Verificar que el numero sea entero positivo
        if num_usuario < 0:
            print("---> Se necesita un numero positivo entero (Mayor o igual a ZERO), Inténtalo de nuevo <---")
        elif num_usuario == 0 or num_usuario == 1:
            print("El factorial de ", num_usuario," es", numero_factorial)
        # Operacion para obtener el factorial
        else:
            for i in range(1, num_usuario+1):
                numero_factorial = numero_factorial*i
            print ("El factorial del número",num_usuario,"es",numero_factorial)
             # Crear documento, escribir resultado y cerrar 
            output_file = open("output_file_factorial.txt", "a")
            output_file.write(f"El factorial de {num_usuario} es: {numero_factorial}\n")
            output_file.close()

        # Preguntar al usuario si desea continuar
        continuar = str(input("Indique (Y/N) para ingresar un nuevo numero: "))
        continuar = continuar.upper()
        if continuar == "N":
            print("Gracias!!!")
            break
        else:
            continue
