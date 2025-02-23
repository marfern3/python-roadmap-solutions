# Funciones básicas

def function1 ():
    print("Esta es una función sin parametro ni retorno")

def function2 (i):
    print("El número recibido es:", i)

def function3 (i, x):
    print("Esto son dos parámetros", i, x)

def function4 (i = 4):
    print("La suma de 2 + 2 es igual a:", i)
    return(i)

resultado = function4()
print ("La operación es = ", resultado)

# Funciones dentro de funciones
def function_ext (i = 1):
    if i == 1 :
        def function_int (x):
            return("Esta es la funcion interna")
        return (function_int(i))
    else:
        return("La función interna no ha funcionado")

resultado = function_ext()
print(resultado)

# Función ya existente en Python
def number_sum ():
    n1 = float(input ('¿Él primer número és?:'))
    n2 = float(input ('¿Él segundo número és?'))
    resultado = (n1 + n2)
    return resultado

suma = number_sum()
print(suma)

# Variables locales y globales

mensaje = 'Esto es una variable global'

def var_global ():
    print ('Accedo a la variable global', mensaje)

def modif_global():
    global mensaje
    mensaje = ('He modificado la variable global')
    print ('Ahora la variable global es:', mensaje)

def var_local ():
    text = ('Esto es una variable local')
    print ('Accedo a la variable local', text)

var_global()
modif_global()
var_local()

print('Variable global final:', mensaje)

# FizzBuzz modificado
def fizz_buzz():
    contador = 0
    for n in range (1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print ('FizzBuzz')
        elif n % 3 == 0:
            print ('Fizz')
        elif n % 5 == 0:
            print ('Buzz')
        else:
            print(n)
            contador += 1

    return contador

resultado = fizz_buzz()
print ('Cantidad de números impresos es:', resultado)