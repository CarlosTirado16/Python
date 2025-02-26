#Variables

my_string_variable= 'Mi string'
print(my_string_variable)
#Para escribir una variable se recomienda hacerlo en minusculas 

my_int__variable=4
print(my_int__variable)

my_bool__variable=True
print(my_bool__variable)

print(my_bool__variable, my_int__variable, my_string_variable)
print("2+2=",my_int__variable)
#Se pueden poner distintas variables en un prints poniendo comas

my_int_to_str__variable= str(my_int__variable)
print(my_int_to_str__variable) 
print(type(my_int_to_str__variable))
#La función str cambia el tipo de dato a str

#Len nos da el número de items
print(len(my_string_variable)) #9

#Variables en una sola línea(No abusar)
name, surname, age = "Carlos", "Tirado", 24
print("Me llamo ",name, surname,", mi edad es", age)

#Input
your_name = input('¿Cuál es tu nombre? ')
print("Tú nombre es ",your_name)

#Una variable se puede sobreescribir y cambiar también su tipo
name: str = 24 #Aunque le indiquemos str el tipo sigue siendo int(Python no tiene tipado fuerte)
print(type(name))

price = 9.99
print(int(price)) #Va a redondear hacia abajo

