# Calculadora Matematica

# Definir Funciones

# Funcion de la Operacion Suma
def suma():    
    lista = []
    sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para regresar al Menu de Opciones):"))
    suma_numeros = 0
    while sumar !=0:
        lista.append(sumar)
        sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para regresar al Menu de Opciones):"))
    print("Los numeros ingresados son: ")
    print(lista)
    for total in lista:
        suma_numeros += total
    print(f"El total de la suma de {lista} es:")
    print(suma_numeros)
#suma()

# Funcion de la Operacion Resta
def resta():
    resta_uno = int(input("Ingrese el primer Numero: "))
    resta_dos = int(input("Ingrese el segundo Numero: "))
    total = resta_uno - resta_dos
    print(f"La resta de ambos valores es: {total}.")
#resta()

#INICIA MENU

menu = {}
menu['2']="Resta"
menu['3']="Multiplicación"
menu['7']="SALIR"
menu['1']="Suma"
menu['5']="Factorial"
menu['6']="Potencia"
menu['4']="División"

while True:
    print("\n<--- Menu de Opciones --->")
    options=menu.keys()
    #options.sort() #ni idea que hace este sort ---> Este sort ya no se utiliza asi(Ver linea 43)
    for entry in sorted(options): # Esta es la menera correcta para odernar las llaves del dicionario
        print (entry, menu[entry])
    selection=input("Please Select:")
    if selection =='1': # Suma
        suma() # Invocacion de la funcion suma()
    elif selection == '2': # Resta
        resta() # Invocacion de la funcion resta()
    elif selection == '3':
        print ("\n Multiplicación \n")
    elif selection == '4':
        print ("\n División \n")
    elif selection == '5':
        print ("\n Factorial \n")
    elif selection == '6':
        print ("\n Potencia \n")
    elif selection == '7':
        print("Muchas Gracias! \n")
        break
    else:
        print ("\n Opción no válida \n" )
      #LINEA DE PRUEBA
      #LINEA DE PRUEBA 02
      #LINEA DE PRUEBA 03