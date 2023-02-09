def eliminar_elemento(lista, valor):
    while valor in lista:
        lista.remove(valor)
    return lista

datos = []
while True:
    entrada = input("Ingrese un valor (escriba 'fin' para terminar): ")
    if entrada == 'fin':
        break
    else:
        datos.append(entrada)
valor_eliminar = input("Ingrese el valor a eliminar: ")
resultado = eliminar_elemento(datos, valor_eliminar)
print("Lista sin el elemento '%s': %s" % (valor_eliminar, resultado))
