# conversion de cadena a enteros
cadena_a_entero=int("2024")
print(cadena_a_entero)

# Conversión de cadena a flotante
cadena_a_flotante = float("18.0")
print(cadena_a_flotante)

# Conversión de número a cadena
numero_a_cadena = str(4568)
print(numero_a_cadena)

# Multilíneas de cadenas usando triple comillas
texto_multilinea = """Este es un ejemplo como python imprime con 3 comillas"""
print(texto_multilinea)

# Uso de la función len() para obtener la longitud de una cadena
mi_cadena = "Hola mundo aqui estamos aprendiendo python 2024"
longitud = len(mi_cadena)
print("Longitud de la cadena:", longitud)

#Obteber los primeros n caracteres de una cadena
n= 10
cadena = "hola mundo 2024"
primeros_n = cadena[:n]
print("Primeros", n, "caracteres:", primeros_n)

#obtener caracateres en medio de una cedena
inicio = 5
fin = 10
medio = cadena[inicio:fin]
print("Caracteres de en medio:", medio)

#obtener los ultimos caracteres de una cadena
n = 5
ultimos_n = cadena[-n:]
print("Últimos", n, "caracteres:", ultimos_n)

#Funcion upper
# Convertir una cadena a mayúsculas
cadena = "juan carlos tidpaz bolaños"
cadena_mayus = cadena.upper()
print("Cadena en mayúsculas:", cadena_mayus)

# Convertir una cadena a minúsculas
cadena = "JUAN CARLOS TIDPAZ BOLAÑOS"
cadena_minus = cadena.lower()
print("Cadena en minúsculas:", cadena_minus)

# Uso de cadenas multilínea con comillas triples
texto_multilinea = """Esta es una cadena
que ocupa varias líneas.
----hola mundo------
----python 2024-----
----juan carlos------"""
print(texto_multilinea)

# Eliminación de espacios en blanco al principio y al final de una cadena
cadena_con_espacios = "     Hola, mundo estamos aprendiendo python   "
cadena_sin_espacios = cadena_con_espacios.strip()
print("Aqui vemos la Cadena sin espacios:", cadena_sin_espacios)

# Reemplazar un texto específico por otro
cadena_original = "juan carlos le gusta el futbol en sintetica"
cadena_reemplazada = cadena_original.replace("juan", "le gusta")
print("Cadena reemplazada:", cadena_reemplazada)

# Dividir una cadena en una lista de palabras
cadena = "hola mundo estamos aprendiendo python"
lista_palabras = cadena.split()
print("Lista de palabras:", lista_palabras)

# Uso de f-strings para formatear cadenas
nombre = "juan carlos tidpaz bolaños"
edad = 32
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)  # Salida: 'Hola, mi nombre es Ana y tengo 25 años.'



