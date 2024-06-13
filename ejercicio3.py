'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''

def longitud (lista):
    contador = 0
    for i in lista:
        contador +=1 
    return (contador)

largo= longitud ("lista")
dos=["Hola como esta", 34, "abc"]

print (f"El valor de la primera iteración es {largo}, el valor de la segunda es {longitud (dos) }")