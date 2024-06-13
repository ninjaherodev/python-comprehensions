from itertools import zip_longest
import json
numbers = [1,2,3,4]

number_x2 = []
for i in numbers:
  number_x2.append(i*2)
print(numbers)

numsx2 = list(map(lambda x: x*2, numbers))
print('v1:',number_x2)
print('v2:',numsx2)

mapi = lambda func, x: [func(i) for i in x]
numsx3 =mapi(lambda x: x*2,numbers)
print('v3:',numsx3)
print(mapi(str, [1, 2, 3, 4]))
print(mapi(len, ["apple", "banana", "cherry"]))


numsA = [1,2,3,4]
numsB = [5,6,7]

result = list(map(lambda x,y: x+y,numsA, numsB))
print(result)
print([a + b for a, b in zip(numsA, numsB)])
print([a + b for a, b in zip_longest(numsA, numsB, fillvalue=0)])


items = [{'product':'camisa', 'price':100},
         {'product':'pantalones', 'price':300},
         {'product':'medias', 'price':200}]


precios1 = [item['price'] for item in items]
precios2 = list(map(lambda item: item['price'], items))
print('precios 1:', precios1)
print('precios 2:', precios2)

def add_taxes(item):
  modified_item = item.copy()
  modified_item['taxes'] = modified_item['price'] * .19
  return modified_item
items_with_tax = list(map(add_taxes, items))

print(json.dumps(items, indent=4))
print(json.dumps(items_with_tax, indent=4))
