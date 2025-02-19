"""
 Crea una única función (importante que sólo sea una) que sea capaz
 de calcular y retornar el área de un polígono.
 - La función recibirá por parámetro sólo UN polígono a la vez.
 - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 - Imprime el cálculo del área de un polígono de cada tipo.
 """

def calcular_area(poligono, base , altura=0):
    if poligono.lower()== "triangulo":
        if altura == 0:
            print("Necesito la altura del triangulo")
        else:
            print("El area del tringulo es:", base*altura/2)
    if poligono.lower()== "cuadrado":
        print("El area del cuadrado es:", base**2)
    if poligono.lower()== "rectangulo":
        if altura == 0:
            print("Necesito la altura del rectangulo")
        else:
            print("El area del rectangulo es:", base*altura)

calcular_area("RECTANGULO")