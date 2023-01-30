#Lista al cubo: Escriba un programa que cree una lista de números y la
##imprima. Luego debe imprimir dicha lista pero con cada valor convertido en su cubo

lista=[2,4,8,16]
 
print ("Lista original", lista)
 
for i in range(0,len(lista)):
	lista[i]=lista[i]*lista[i]*lista[i]
 
print ("El cubo de la lista es", lista)