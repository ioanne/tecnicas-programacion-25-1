variable = 10

# Tipos de datos

# Numeros enteros (int) integer
10

# Numeros decimales (flotantes) float
10.5

# Boolean Verdadero / Falso  True False
True
False

# Cadena de texto str string
"Hola, esto es una cadena de texto"
'Hola, esto es una cadena de texto'

"hola"

print("Hola esta es la comilla siemple ' ")


print('Hola esta es la comilla doble " ')



# El dato que se usa cuando no hay nada
None # En otros lenguajes se usa null

print(None)

numero = None
cadena_texto = None

# Almacenar 10 en memoria y guardarlo en variable para reutilizar
valor_1 = 10

# Almacenar 30 en memoria y guardarlo en variable para reutilizar
valor_2 = 30


# Accedemos a los valores guardados en memoria anteriormente.
resultado = valor_1 + valor_2

resultado_2 = (10 + 5) / 4 * 2 + 2
resultado_3 = 10 + 5 / 4 * 2 + 2

print(resultado)

print(10 / 30)

# hexadecimal = F

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,   11, 12,     13,     14,     15

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A,    B,  C,      D,      E,      F



edad = 14
nombre = "Juan"


# Operadores de comparación
# indentación
if edad > 15:
    print("tiene más de 15 años")
    print("otra linea")
    print("otra linea")
elif edad == 15:
    print("tiene 15 años")
else:
    print("No tiene 15 años o mas")



if edad == 14 and nombre == "Juan":
    print("Juan tiene 14 años")


print(bool(10 and 0 or 1 and 0))


print(bool(10 * 0 + 1 * 0))

# 0 evalua falso
# mas de cero evalua verdadero
# menos de cero evalua verdadero
# None evalua falso
# "" evalua falso
# "Hola" evalua verdadero
# 0.0 evalua falso
# 0.1 evalua verdadero


print(bool(-10))

print(bool(""))

print(bool(0))

print(bool(None))

print(bool(0.0))