'''Division'''

# Esta es una funcion para dividir dos numeros ingresados por un usuario
# El usuario debe ingresar dos numeros
# El resultado de la division se guarda en el file "output_file_division.txt"

def division():
    '''Funcion para Dividir'''
    while True:
        # Recibir Numeros enteros del usuario
        primer_numero = int(input("Ingrese el primer numero que desea dividir: "))
        segundo_numero = int(input("Ingrese el segundo numero que desea dividir: "))
        total = primer_numero // segundo_numero
        # Imprimir resultado de la division
        print(f"La division entre ambos numeros es: {total}")
        # Abre/Crea un documento en modo "append"
        output_file = open("output_file_division.txt", "a")
        # Agrega el resultado al documento existente
        output_file.write(f"El resultado de la division de {primer_numero} // {segundo_numero} es: {total}\n")
        # Cierra el documento
        output_file.close()
        # Preguntar al usuario si desea continuar
        continuar = str(input("Indique (Y/N) para continuar: "))
        continuar = continuar.upper()
        if continuar == "N":
            print("\nGracias!")
            break
