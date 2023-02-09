def eliminar_elemento(lista, elemento):
    while elemento in lista:
        lista.remove(elemento)
    return lista

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 3, 6, 3]
print(eliminar_elemento(mi_lista, 3)) # [1, 2, 4, 5, 6]
