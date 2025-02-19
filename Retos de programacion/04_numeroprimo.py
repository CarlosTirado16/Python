"""
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
"""
listaprimos = list()
numero = 2  
total = 100

while numero <= total:
    es_primo = True
    for i in range(2, numero):  # Recorremos hasta la raíz cuadrada del número
        if numero % i == 0:
            es_primo = False
            break  # Si es divisible, no es primo y salimos del bucle
    
    if es_primo:
        listaprimos.append(numero)  # Solo agregamos si es primo
    
    numero += 1

print(listaprimos)

