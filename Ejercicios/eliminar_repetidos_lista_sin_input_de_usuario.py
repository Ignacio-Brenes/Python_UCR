#Eliminar los valores repetidos de una lista
test_list = [1, 1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]
def eliminar_reps(list):
    res = []
    for item in list:
        if item not in res:
            res.append(item)
    return res
print("\n")    
print("La lista sin valores repetidos es: \n") 
print(eliminar_reps(test_list))
print("\n") 