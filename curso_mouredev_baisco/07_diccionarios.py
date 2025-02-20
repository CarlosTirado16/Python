### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Carlos",
                 "Apellido": "Tirado", "Edad": 24, 1: "Python"} #Se tiene que poner los : para diferenciarlo de un set

my_dict = {
    "Nombre": "Carlos",
    "Apellido": "Tirado",
    "Edad": 24,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.85  #Se pueden usar distintos tipos de datos de ambos lados
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1]) #1.85
print(my_dict["Nombre"])  #Carlos, nos devuelve los valores


print("Tirado" in my_dict) #False
print("Apellido" in my_dict) #True, es por clave

# Inserción

my_dict["Calle"] = "Calle Chumi"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) #Cambia el valor

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) #Diccionario sin valres pero con las claves
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Tirado") #Pone todos los valores como Tirado
print((my_new_dict)) 

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))