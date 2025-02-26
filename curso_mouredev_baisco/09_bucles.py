### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [16, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (24, 1.85, "Carlos", "Tirado")

for element in my_tuple:
    print(element)

my_set = {"Carlos", "Tirado", 24}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Carlos", "Apellido": "Tirado", "Edad": 24, 1: "Python"} #Me imprime las claves

for element in my_dict:
    print(element)
    if element == "Edad":
        break #No se imprime el else porque se interrumpe
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue #No se imprime en edad
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")

for i in range(3):
    print(i) #0,1,2

