#Factorial del número dado: Escriba un programa en el que dado un número
#por el usuario, imprima el factorial (!) de dicho número.
#Ejemplo: input: 5, resultado: 120

def factorial(num):
    fact = 1
    for i in range(1, num):
        fact += fact * i
    return fact
 
 
numero = int(input('Ingrese un numero'))
print('Su factorial es :', factorial(numero))