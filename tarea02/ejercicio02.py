#->-> No logré darle el formato solicitado <-<-
#Triángulo: Escriba un programa que reciba un número del usuario y
#despliegue en pantalla el siguiente patrón de números llegando hasta el
#número elegido:

def numbersbefore(num):
    return [(num - x) for x in range(1, num)];

def getuseraction():
    userNumber = int(input("Introduce el número"));
    return numbersbefore(userNumber);

print(getuseraction());