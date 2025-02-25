def operaciones_cadenas():
    cadena = 'Hola, Mundo'
    print('La cadena Original es:', cadena)

    #Acceso a caracteres individuales.
    print('El primer carácter es:', cadena[0])
    print('El último carácter es:', cadena[-1])

    # Obtención de subcadenas.
    print('Subcadena (tres primeros caracteres)', cadena[0:3])
    print('Subcadena (tres últimos caracteres))', cadena [-3:])

    # Longitud de cadenas.
    print ('La longitud de la cadena es:', len(cadena))

    # Concatenación.
    cadena2 = '¿Cómo están?'
    print('La concatenación de las cadenas es:', cadena + cadena2)

    # Repetición.
    print('Repetiremos la cadena 3 veces:', cadena * 3)

    # Recorrido de cada carácter.
    print('Recorrido de carácter:')
    for caracter in cadena:
        print(caracter, end = ' ')
    print()

    # Conversión a mayúsculas y minúsculas.
    cadena_minus = 'este texto está en minúsculas:'
    print('Conversión a mayúsculas', cadena_minus.upper())
    cadena_mayus = 'ESTE TEXTO ESTÁ EN MAYÚSCULAS'
    print('Conversión a minúsculas:', cadena_mayus.lower())

    # Reemplazo.
    remplazo = cadena.replace('Hola', 'Adiós',)
    print("Reeplazado ('Hola' por 'Adiós'):", remplazo)

    # División.
    dividido = cadena.split(",")
    print("División (split por ','):", dividido)

    # Unión.
    lista_palabras = ['Todo', ' bien']
    unido = ''.join(lista_palabras)
    print('Unión (join):', unido)

    # Interpolación.
    exclamacion = '!'
    cadena_final = f'Hola, mundo {exclamacion}'
    print('Interpolación (f-string):', cadena_final)

    # Verificaciones.
    print (cadena)
    contiene_mundo = 'Mundo' in cadena
    inicio_hola = cadena.startswith('Hola')
    final_exclamacion = cadena.endswith('!')
    print('Contiene la palabra mundo:', contiene_mundo)
    print("La palabra inicia con 'Hola':", inicio_hola)
    print("La palabra termina con exclamación:", final_exclamacion)
operaciones_cadenas()

# Analisis de palabras.
def is_palindromo (palabra):
    '''Devolvera TRUE o FALSE dependiendo si la palabra es palíndromo o no.'''
    palabra_normalizada = palabra.replace(" ", "").lower()
    return palabra_normalizada == palabra_normalizada[::-1]

def is_anagrama (palabra1, palabra2):
    '''Devolvera TRUE o FALSE dependiendo si la palabra 1 y la palabra 2 es anagrama o no.'''
    p1 = sorted(palabra1.replace(" ", "").lower())
    p2 = sorted(palabra2.replace(" ", "").lower())
    return p1 == p2

def is_isograma (palabra):
    """Devuelve True si 'palabra' es un isograma (todas las letras son únicas)."""
    palabra_normalizada = palabra.replace(" ", "").lower()
    letras = set()
    for letra in palabra_normalizada:
        if letra in letras:
            return False
        letras.add(letra)
    return True

def analizar_palabras(palabra1, palabra2):
    print('Analisis de palabras:')
    print("Palabra 1:", palabra1)
    print("Palabra 2:", palabra2)
    print()
    
    print("¿La palabra 1 es palíndromo?", is_palindromo(palabra1))
    print("¿La palabra 2 es palíndromo?", is_palindromo(palabra2))
    print("¿Son anagramas?", is_anagrama(palabra1, palabra2))
    print("¿La palabra 1 es isograma?", is_isograma(palabra1))
    print("¿La palabra 2 es isograma?", is_isograma(palabra2))

palabra1 = input('Dime la primer palabra: ')
palabra2 = input('Dime la segunda palabra: ')
analizar_palabras(palabra1, palabra2)

    