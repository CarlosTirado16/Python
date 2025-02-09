### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

my_scape_string = "\\tEste es un String \\n escapado" #Para evitar la tabulación y el salto de línea, %.digitos para mayor precision
print(my_scape_string)
#Ejemplo 30 días de python
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote



# Formateo 

name, surname, age = "Carlos", "Tirado", 24
#Distintas formas de hacerlo, todas compilan lo mismo
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) #%d para entero y %f para flotantes
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado
language = "python"
a, b, c, d, e, f = language #Tenemos que llenar todos los caracteres
print(a) #P
print(e) #O

#Division
language_slice = language[1:3] #yt
print(language_slice)

language_slice = language[1:] #ython
print(language_slice)

language_slice = language[-2] #o
print(language_slice)

language_slice = language[0:6:2] #pto (Caracteres pares)
print(language_slice)

# Reversa

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) #Primera mayuscula
print(language.upper()) #Mayusculas
print(language.count("t")) #Cuenta cuantas veces aparece cierto caracter
print(language.isnumeric()) #¿Es número? Falso
print("1".isnumeric()) #True
print(language.lower()) #Minusculas
print(language.lower().isupper()) #¿Son mayusculas? Falso
print(language.startswith("Py")) #Empieza con Py, Falso, la primera es minuscula
print("Py" == "py")  # No es lo mismo
text = "12345"
print(text.isnumeric())