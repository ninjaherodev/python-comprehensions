set_countries={'col','mex','bol','col'}
print(set_countries)
print(type(set_countries))

set_countries={1,2,2,443,23}
print(set_countries)

set_types={1,'hola',False,12.2}
print(set_types)

set_from_string=set('hola')
print(set_from_string)

set_from_tupla=set(('abc','cbv','as','abc'))
print(set_from_tupla)

list_number =[1,2,3,1,2,3,4]
set_from_list=set(list_number)
print(set_from_list)

unique_number=list(set_from_list)
print(unique_number)