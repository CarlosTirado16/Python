### Errores ###

numberOne = 5
numberTwo = 2
numberTwo = "4000"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error") #Si no hay errores se muestra este
except:
    print("Se ha producido un error") #Si hay errores muestra este mensaje
else:
    print("La ejecucción continua") #Se muestra si se ejecuta el try correctamente
finally: 
    print("Hola") #Se ejecuta en cualquier caso


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error") 
except ValueError:  #Podemos elegir que error va a evaluar
    print("Se ha producido ValueError") 
except TypeError:
    print("Se ha producido un TypeError")


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error") 
except ValueError as error:  #Podemos guardar la información del error
    print(error)
except Exception as excepcion:
    print(excepcion) #Me captura alguna excepcion que se puede dar

def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError(
                "No se puede calcular la raiz cuadrada de un numero negativo.")
        return number ** 0.5
    except ValueError as e:
        print(f"Error: {e}")

raiz = calculate_square_root(10)
print(raiz)

   

