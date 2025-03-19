# Tipos de datos
# string, integer, boolean, float, None

cadena1 = "Cadena de texto"
cadena2 = 'Cadena de texto'

numero = 1
decimal = 1.0

vacio = None

booleano = True
booleano2 = False


# Operadores de comparación
# ==    !=     >     <     >=    <=

condicion = False
# Es un solo bloque
if condicion == True:
    # Muchas cosas a ejecutar
    print("La condición es verdadera")
elif condicion == None: # else if
    # Muchas cosas a ejecutar
    print("La condición esta vacia")
else:
    print("La condición es falsa")
# Fin del bloque

# ...
# ...
# ...

es_verdadero = None

if es_verdadero:
    print("Es verdadero")
elif es_verdadero is None:
    print("No podemos evaluar")
elif not es_verdadero: # Si viene verdadero se convierte en falso
    print("algo1")


# if anidado
if es_verdadero is not None:
    if es_verdadero:
        print("Es verdadero")
    else:
        print("algo1")




print(bool(not True))
print(bool(not False))
print(bool(not 0)) # 0 evalua falso


# while True:
# Nos pide un numero y nosotros lo ingresamos
numero = input("Ingresar valor: ") # Nos devuelve TEXTO
# Convertimos el valor que recibimos en un numero entero
if numero:
    # Convierte lo que recibe en un numero entero
    numero_entero = int(numero)
    if numero_entero > 10:
        print("El valor es mayor que 10")
    elif numero_entero > 5:
        print("El valor es mayor a 5 y menor o igual a 10")
    else:
        print("No es mayor a 5.")


texto = input("Ingresar texto: ")

# Convertir valores
texto = int(texto)
print(type(texto))


# Funciones de python

# int -> Convierte un valor en entero
# float -> Convierte un valor en un numero decimal/flotante
# type -> Nos dice de que tipo es un dato
# print -> Muestra un texto por pantalla
# input -> Recibe un valor POR TECLADO

# Como se usan las funciones


# Palabras reservadas

# if, for, while, in, is, not, or, and

