# Autor: Alejandro Flores Jacobo 
# Fecha: 02-03-2023
# Descripcion: 
# Script para obtener el total de caracteres de una archivo txt 
# para sacar entropia de acuerdo al orden de la fuente.

import math

titulo = 'Grimms’ Fairy Tales, by Jacob Grimm and Wilhelm Grimm_pr'
# Abrir el archivo de texto y leer su contenido
with open(titulo + '.txt', 'r') as f:
    contenido = f.read()

# Inicializar un diccionario vacío para almacenar los resultados
resultados = {}

# Archivo para guardar entropias
entropias = open('Entropias', 'w')

# Convierte todo el contenido a minúsculas
contenido = contenido.lower()

# Recorrer cada carácter en el contenido del archivo
for caracter in contenido:
    # Comprobar si el carácter es imprimible y si no es un espacio en blanco
    if caracter.isprintable() and not caracter.isspace():
        # Si el carácter ya está en el diccionario, incrementar su valor en 1
        if caracter in resultados:
            resultados[caracter] += 1
        # Si el carácter no está en el diccionario, agregarlo con un valor de 1
        else:
            resultados[caracter] = 1

# Agregar la cantidad de espacios en el diccionario
espacios = contenido.count(' ')
resultados[' '] = espacios

# Ordenar los elementos del diccionario por valor de mayor a menor y asignarlos a una lista de tuplas
ordenado = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

# Abrir el archivo en modo escritura
archivo = open("numero de caracteres.txt", "w")

# Recorrer el diccionario e imprimir cada par clave-valor
for tupla in ordenado:
        # Escribir en el archivo
        archivo.write(str(tupla[0])+', '+str(tupla[1])+'\n')
archivo.close()  

for tupla in ordenado:
    print(tupla[0], tupla[1])
# Imprimir las probabilidades de cada carácter de mayor a menor
simbolo = 0  #simbolo
hX = 0       #entropia

# Primer orden
primer_orden ={}

# Abrir el archivo en modo escritura
archivo = open("probabilidades_primer_orden.txt", "w")

for caracter, conteo in ordenado:

    #se calcula la probabilidad
    probabilidad = conteo / len(contenido)
    # Calculo para la entropia en primer orden 
    hX += probabilidad * math.log2(1/probabilidad)

    # se agrena los datos al diccionario para utilizar las pobabilidades en ordenes siguientes
    primer_orden['x'+ str(simbolo)] = probabilidad
    # Escribir en el archivo
    archivo.write('x'+ str(simbolo)+", "+str(probabilidad)+"\n")
    simbolo += 1
archivo.close() 

entropias.write('n1, '+ str(hX)+'\n')


# Segundo orden
segundo_orden = {}
hX = 0

# Abrir el archivo en modo escritura
archivo = open("probabilidades_segundo_orden.txt", "w")


# Recorrer el diccionario e imprimir cada par clave-valor
for clave, valor in primer_orden.items():
    for clave1, valor1 in primer_orden.items():
        probabilidad = valor*valor1
        segundo_orden[clave+clave1] = probabilidad
        # Escribir en el archivo
        archivo.write(str(clave+clave1)+", "+str(probabilidad)+"\n")
        # Calculo para la entropia en primer orden 
        hX += probabilidad * math.log2(1/probabilidad)

archivo.close()     
entropias.write('n2, '+ str(hX)+'\n')

# Segundo orden
tercer_orden = {}
hX = 0

# Abrir el archivo en modo escritura
archivo = open("probabilidades_tercer_orden.txt", "w")

# Recorrer el diccionario e imprimir cada par clave-valor
for clave, valor in segundo_orden.items():
    for clave1, valor1 in segundo_orden.items():
        probabilidad = valor*valor1
        tercer_orden[clave+clave1] = probabilidad
        # Escribir en el archivo
        archivo.write(str(clave+clave1)+", "+str(probabilidad)+"\n")
        # Calculo para la entropia en primer orden 
        hX += probabilidad * math.log2(1/probabilidad)
archivo.close() 

entropias.write('n3, '+ str(hX)+'\n')
entropias.close()

