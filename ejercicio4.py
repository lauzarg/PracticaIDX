'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

def vocal (letra):
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        return True
    else:
        return False

def vocal2 (letra):
    vocales = "aeiou"
    if letra in vocales:
        return True
    else:
        return False

letra = input ("ingrese una letra: ")

print (vocal2 (letra)) 
