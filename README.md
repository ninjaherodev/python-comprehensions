# The Zen of Python

The Zen of Python is a collection of principles that guide the design of the Python programming language. These principles are presented as a short poem and can be viewed in any Python interpreter by typing `import this`.

El Zen de Python es una colección de principios que guían el diseño del lenguaje de programación Python. Estos principios se presentan como un poema corto y se pueden ver en cualquier interpretador de Python escribiendo

```python
import this
```

## Zen of Python

```plaintext
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

# Sets

En Python, un "set" (conjunto) es una colección desordenada y mutable de elementos únicos. Esto significa que un conjunto no contiene elementos duplicados y puede cambiar (es mutable), pero no tiene un orden definido. Los conjuntos se utilizan comúnmente cuando se necesita almacenar elementos únicos y realizar operaciones como unión, intersección, diferencia y comprobación de pertenencia de manera eficiente.

Puedes crear un conjunto en Python utilizando llaves {} o la función set(), proporcionando una lista de elementos entre ellas. Por ejemplo:

```python
# Crear un conjunto con llaves
mi_set = {1, 2, 3, 4, 5}

# Crear un conjunto con la función set()
mi_otro_set = set([1, 2, 3, 4, 5])
```

Los conjuntos no admiten elementos duplicados, por lo que si intentas crear un conjunto con elementos duplicados, Python eliminará automáticamente los duplicados:

```python
mi_set = {1, 2, 2, 3, 3, 4, 5}
print(mi_set)  # Resultado: {1, 2, 3, 4, 5}
```

Los conjuntos en Python admiten varias operaciones comunes, como agregar elementos, eliminar elementos, comprobar la pertenencia de un elemento, calcular la unión, la intersección, la diferencia, etc. Por ejemplo:

```python
mi_set = {1, 2, 3}
mi_set.add(4)        # Agregar un elemento
mi_set.remove(2)     # Eliminar un elemento

print(3 in mi_set)   # Comprobar si un elemento está en el conjunto (True)
print(5 in mi_set)   # Comprobar si un elemento está en el conjunto (False)

otro_set = {3, 4, 5}
union = mi_set | otro_set         # Unión de conjuntos
interseccion = mi_set & otro_set  # Intersección de conjuntos
diferencia = mi_set - otro_set    # Diferencia de conjuntos

print(union)         # Resultado: {1, 3, 4, 5}
print(interseccion)  # Resultado: {3, 4}
print(diferencia)    # Resultado: {1}
```

En resumen, los conjuntos en Python son colecciones desordenadas y mutables de elementos únicos que son útiles cuando necesitas almacenar elementos únicos y realizar operaciones de conjuntos eficientemente.

# Funciones Set

- add(): Añade un elemento.
- update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
- discard(): Elimina un elemento y si ya existe no lanza ningún error.
- remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
- pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
- clear(): Elimina todo el contenido del conjunto.

```python
set_countries = {'col', 'mex', 'bol'}
set_countries_two = {'cl', 'br', 'col'}
set_countries_three = {'ur', 've'}

set_countries.update(set_countries_two, set_countries_three)

print(set_countries)
```

# Operaciones Set

- union(set): Realiza la operacion “union” entre dos conjuntos. La unión entre dos conjuntos es sumar los elementos de estos sin repetir elementos. Esta operación tambien se puede realizar con el signo “|”: set_a | set_b.

- intersection(set): Realiza la operacion “intersection” entre dos conjuntos. La intersección entre dos conjuntos es tomar unicamente los elementos en común de los conjutnos. Esta operación tambien se puede realizar con el signo “&”: set_a & set_b.

- difference(set): Realiza la operacion “difference” entre dos conjuntos. La diferencia entre dos conjuntos es restar los elementos del segundo conjunto al primero. Esta operación tambien se puede realizar con el signo “-”: set_a - set_b.

- symmetric_difference(set): Realiza la operacion “symmetric_difference” entre dos conjuntos. La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos exceptuando el elemento en común. Esta operación tambien se puede realizar con el signo “^”: set_a ^ set_b.

NOTA: No se pueden realizar operaciones con otras colecciones de datos, solo se puede únicamente entre conjuntos.

# Pueba Set

Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.

Este algoritmo recibirá como entrada cuatro conjuntos de países, estos países serán de todo el continente americano divididos de la siguiente manera:

countries - Países del continente en general.
northAmerica - Países del norte de América.
centralAmerica - Países del centro de América.
southAmerica - Países del sur de América.
En resumen, el algoritmo deberá eliminar los elementos repetidos de los cuatro conjuntos de países y obtener un conjunto único llamado new_set.

Ejemplo 1:

```python
#Input:
{"MX", "COL", "ARG", "USA"},
{"USA", "CA"},
{"MX", "GT", "BZ"},
{"COL", "BZ", "ARG"}

#Output:
{'ARG', 'USA', 'CANADA', 'GT', 'COL', 'MX', 'BZ'}
```

Ejemplo 2:

```python
#Input:
{"BOL"},
{"CA"},
{"MX"},
{"COL"}

#Output:

{'COL', 'CA', 'BOL', 'MX'}
```

## Solución

```python
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
countries = {"MX", "COL", "ARG", "USA"}
new_set = countries | northAm | centralAm | southAm
#new_set.update(countries,northAm,centralAm,southAm)
print(new_set)
```
