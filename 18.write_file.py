
#Ojo cuando tengo r+ modifico el archivo adicionado al final
#cuando uso w+ el sobre escribe todo el archivo
with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')
    file.write('otra linea\n')
    file.write('otra linea\n')