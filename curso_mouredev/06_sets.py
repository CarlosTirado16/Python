### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Carlos", "Tirado", 24}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("B")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("B")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Carlos" in my_other_set)
print("Charlie" in my_other_set)

# Eliminación

my_other_set.remove("Carlos")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Carlos", "Tirado", 24}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))