set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b) # set_a | set_b
print(set_c)
print(set_a | set_b)

set_d = set_a.intersection(set_b) # set_a & set_b
print(set_d)
print(set_a & set_b)


set_e = set_a.difference(set_b) # set_a - set_b
print(set_e)
print(set_a - set_b)

set_f = set_a.symmetric_difference(set_b) # set_a ^ set_b
print(set_f)
print(set_a ^ set_b)