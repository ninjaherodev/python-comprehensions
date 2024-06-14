suma = lambda x,y: x+y
assert suma(2,2) == 4
try:
  age = 10
  if age < 18:
      raise Exception('no se permiten menores de edad')
except Exception as error:
  print(error)
try:
  print(0/0)
except ZeroDivisionError as error:
  print(error)
try:
 assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as Error:
  print(Error)
  
print('llego al final')