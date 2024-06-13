# https://github.com/Soyagvs/exercices-python/tree/main

'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''

def max_de_tres (num1, num2, num3):

    if num1==num2 or num1==num3 or num2==num3:
        return print ("Hay numeros que son iguales")
        
    if num1>num2 and num1>num3:
        return print (f"el mayor de los tres es {num1}")
    
    elif num2>num1 and num2>num3:
        return print (f"el mayor de los tres es {num2}")
    else:
        return print (f"el mayor de los tres {num3}")


num1=int(input("Ingrese un numero"))
num2=int(input("ingrese otro número"))
num3=int(input("ingrese un último número"))

max_de_tres (num1, num2, num3)
