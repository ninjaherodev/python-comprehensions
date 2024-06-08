lista = [1,2,3,4,5]
util= [7,8,9,10]

#tenemos funciones para adicionar elementos
lista.append(6)
lista.insert(2, 3)
lista.extend(util)

#Funciones para eliminar
lista.remove(3) 
lista.pop() #lista.pop(2)
del lista[1:3]
#list.clear()

# Devuelve el índice de la primera aparición de un elemento.
print('index:',(lista.index(7)))
#Devuelve el número de apariciones de un elemento en la lista.
print('count:',(lista.count(7)))
#Ordena los elementos de la lista en su lugar.
print('sort:',(lista.sort()))
#Invierte el orden de los elementos de la lista en su lugar.
print('reverse:',(lista.reverse()))

print('lista:',lista)
print('tamaño de la lista:',len(lista))
print('max:',max(lista))
print('min:',min(lista))
print('sum:',sum(lista))
print('sorted:',sorted(lista, reverse=True))
print('reversed:',list(reversed(lista)))

print(lista)
list_multi = []
for item in lista:
  list_multi.append(item*2)
print(list_multi)

#list_v2 =[element * 2 for element in list]
list_v2 = [element * 2 for element in lista if element % 2 == 0]
print(list_v2)

# Matriz de 3x3 con comprensión anidada
matriz = [[j for j in range(3)] for i in range(3)]
print(matriz)  # Salida: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Conjunto de números pares
conjunto = {x for x in range(10) if x % 2 == 0}
print(conjunto)  # Salida: {0, 2, 4, 6, 8}

# Diccionario de números y sus cuadrados
diccionario = {x: x**2 for x in range(5)}
print(diccionario)  # Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#Iteradores y expresiones generadoras
numeros = [1,2,3]
letters = ['a', 'b', 'c']
for index,letter in enumerate(letters):
  print(index, letter)

for num,letter in zip(numeros,letters):
  print(num,letter)


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
  print(fila)

filas = len(matriz)
columnas = len(matriz[0])
transpuesta = [[None] * filas for _ in range(columnas)]

print('filas:', filas)
print('columnas:', columnas)
print('transpuesta:', transpuesta)

# traspuesta = [[fila[i] for fila in matriz] for i in range(3)]
# print(traspuesta)

for i in range(filas):
    for j in range(columnas):
      transpuesta[j][i] = matriz[i][j]
      print(matriz[i][j])
print(transpuesta)

trans = [[fila[0] for fila in matriz]]
print(trans)