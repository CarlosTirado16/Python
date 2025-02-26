'''
  Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
 '''

def anagrama(palabra1 , palabra2):
    #Primero corroboramos si tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False
    
    #Despues corrobramos que no sean la misma palabra
    if palabra1 == palabra2:
        return False
    
    #Las hacemos minpusculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    #Definimos dos sets vacíos
    set1 = set()
    set2 = set()

    for letra in palabra1:
        set1.add(letra)

    for letra in palabra2:
        set2.add(letra)

    setanagrama = set1.difference(set2)
    if len(setanagrama) == 0:
        return True
    else:
        return False


esanagramas = anagrama("jAMON", "Monja") #True
print(esanagramas)
esanagramas = anagrama("Carlos", "Charlie") #False
print(esanagramas)