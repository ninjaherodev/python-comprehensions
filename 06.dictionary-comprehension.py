from collections import defaultdict
from collections import OrderedDict
import random
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

mi_diccionario2 = dict(nombre="Juan", edad=30, ciudad="Madrid")

print(mi_diccionario)
print(mi_diccionario2)

#Acceder a los valores de dicciinario
print(mi_diccionario["ciudad"])
print(mi_diccionario.get('nombre'))

mi_diccionario["edad"] = 31
mi_diccionario["profesión"] = "Ingeniero"

del mi_diccionario["ciudad"]
edad = mi_diccionario.pop("edad")
print(mi_diccionario)
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'profesión': 'Ingeniero'}
print(edad)  # Salida: 31

# Utilizando popitem() (elimina el último par clave-valor)
ultimo_item = mi_diccionario.popitem()
print(mi_diccionario)  # Salida: {'nombre': 'Juan'}
print(ultimo_item)  # Salida: ('profesión', 'Ingeniero')


print('diccionario2:',mi_diccionario2)
print(mi_diccionario2.keys())
print(mi_diccionario2.values()) 
print(mi_diccionario2.items())

otro_diccionario = {"peso": 80, "altuta": 152}
mi_diccionario2.update(otro_diccionario)

print('diccionario2:',mi_diccionario2)

print("nombre" in mi_diccionario2)  # Salida: True
print("pais" in mi_diccionario2)    # Salida: False

for clave in mi_diccionario2:
  print(clave)
print('******************+')
for valor in mi_diccionario2.values():
    print(valor)
print('******************+')
# Iterar sobre pares clave-valor
for clave, valor in mi_diccionario2.items():
    print(clave, valor)

copia_diccionario2 = dict(mi_diccionario2)
print(copia_diccionario2)
print(id(copia_diccionario2))
print(id(mi_diccionario2))

diccionario_anidado = {
    "Juan": {"edad": 30, "ciudad": "Madrid"},
    "Maria": {"edad": 25, "ciudad": "Barcelona"}
}

print(diccionario_anidado["Juan"]["ciudad"])  # Salida: Madrid



default_dict = defaultdict(int)
default_dict["a"] += 1
print(default_dict)  # Salida: defaul

ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["a"] = 1
ordered_dict["c"] = 3
print(ordered_dict)  # Salida: OrderedDict([('b', '2'), ('a', '1'), ('c', '3')])




print('dicc2:',mi_diccionario2)
dict = {}
for i in range(1,5):
   dict[i] = i * 2

print(dict)

dict2 = {i: i*2 for i in range(1,5)}
print(dict2)

countries = ['col', 'mex', 'bol', 'pe']
population = {country: 10 for country in countries }
print(population)

names = ['nico', 'zule', 'santi', 'fabio','neyla']
ages = [12, 56, 98]
print(list(zip(names,ages)))


#condicionales en dictionary comprehension
print('condicionales en dictionary comprehension')
paises = ['col', 'mex', 'bol', 'pe']
poblacion = {pais: random.randint(1,100) for pais in paises}
print(poblacion)
print(poblacion.items())

result = {countrie:population for (countrie,population) in poblacion.items() if population > 50}

print(result)

text = 'Hola, Soy Nicolas'
# unique = {c:c.upper() for c in text if c in 'aeiou'}
unique = {c:text.count(c) for c in text if c in 'aeiou'}
print(unique)

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

even =[number for number in numbers if number % 2 == 0]
print('even:', even)
# Ahora usando List Comprehension 👇
even_numbers_v2 = []

print('v2 =>', even_numbers_v2)