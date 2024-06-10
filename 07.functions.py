def find_volume(length=1, width=1, depth=1):
  return length * width * depth, depth, 'Hola' 

result = find_volume()
print(list(result))

volume, depth, saludo = find_volume()
print(volume)
print(depth)
print(saludo)