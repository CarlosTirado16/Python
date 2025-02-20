### Operadores ###

print('Suma: ', 1 + 2)        # 3
print('Resta: ', 2 - 1)     # 1
print('Multiplicación: ', 2 * 3)  # 6
print ('División: ', 4 / 2)       # 2.0  
print('División: ', 6 / 2)        # 3.0         
print('División: ', 7 / 2)        # 3.5 Las divisiones dan números flotantes
print('División sin residuo: ', 7 // 2)   # 3,  
print ('Division sin residuo: ',7 // 3)   # 2  Esta división nos da la división sin el residuo, es int
print('Modulo: ', 3 % 2)         # 1, Me da el residuo
print('Potencia: ', 2 ** 3) # 8 it means 2 * 2 * 2

#Concatenar
print("Hola"+" Python")

#print("Hola"+ 5) No puedo concatenar variables de distinto tipo
print("Hola " + str(5)) #Para concatenar tendría que ser así

print("Hola " * 5) #Se podría multiplicar(Solo para ints)

### Operadores comparativos ###
print(3 > 2)     # True
print(3 >= 2)    # True
print(3 < 2)     # False
print(2 < 3)     # True
print(2 <= 3)    # True
print(3 == 2)    # False, igual a
print(3 != 2)    # True, diferente de

#También sirve para len
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False 

print('tomato' > 'potato')  #True. Esto compara el orden alfabetico

### Operadores lógicos ###
print(3 > 2 and 4 > 3) # True - Los dos son verdaderos
print(3 > 2 and 4 < 3) # False - El segundo es falso
print(3 < 2 and 4 < 3) # False - Ambos son falsos
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - Ambos son true
print(3 > 2 or 4 < 3)  # True - Uno es true
print(3 < 2 or 4 < 3)  # False - Los dos son falsos
print('True or False:', True or False)
print(not 3 > 2)     # False - 3 > 2 es true, el not sería false
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True 
print(not not False) # False

print((5 * 3) + 2 > 10 and (5 * 3) + 2 < 20)