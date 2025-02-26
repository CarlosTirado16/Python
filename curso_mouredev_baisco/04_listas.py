## Listas ##

# Definición
#Es un conjunto de datos donde cada dato ocupa un espacio iniciando en la posición 0'
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [24, 1.85, "Carlos", "Tirado"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4]) #No te puedes pasar
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Carlos"))


age, height, name, surname = my_other_list 
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] #Muy rebuscado
print(age)
print(my_other_list.index(24)) #Se cambia la posición a 0

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list) error

# Creación, inserción, actualización y eliminación

my_other_list.append("B") #Pone un elemento al final
print(my_other_list)

my_other_list.insert(1, "Rojo") #Mete un valor y recorre los demas
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul") #Remueve de la lista 
print(my_other_list)

my_list.remove(30) 
print(my_list)

print(my_list.pop()) #Remueve el ultimo o el que le indiquemos (Se puede almacenar)
print(my_list)

my_pop_element = my_list.pop(2) #Gurda el elemento que sacamos
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy() #La copia

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() #Los voltea
print(my_new_list)

my_new_list.sort() #Ordena de menor a mayor
print(my_new_list)

# Sublistas

print(my_new_list[1:3]) #Los elementos del rango sin contar el último
my_list = [10, 20, 30, 40, 50]
my_sublist = my_list[1:3]
print(my_sublist)

