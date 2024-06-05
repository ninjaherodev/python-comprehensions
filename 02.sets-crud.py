set_countries={'col','mex','bol','col'}
print(len(set_countries))

print('col' in set_countries)
print('pe' in set_countries)

#add
set_countries.add('pe')
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'ar','ecu','pe'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)

#set_countries.remove('arg')
set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))


set_languages = {'javascript','python', 'rush', 'php', 'ruby', 'go', 'java', 'c#'}

# Elementos que deseas eliminar
elementos_a_eliminar = {'python', 'rush', 'php', 'ruby', 'go', 'java', 'c#'}

# Eliminar los elementos 
set_languages -= elementos_a_eliminar

#alternantiva 
# for elemento in elementos_a_eliminar:
#     set_languages.discard(elemento)

print(set_languages) 