file = open('./text.txt')
#print(file.read()) #leo todo el archivo

#leo linea por linea lo malo no se cuantas lineas tiene el archivo
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)
# file.close()


with open('./text.txt') as file:  #la ventaja de esta sintaxis es no preocumarme por cerrar el archivo
    for line in file:
        print(line)