import sys
import re
import time
import collections
print(sys.path)

text = 'mi numero de telefono es 3183895020, el codigo del pais es 57 y mi numero de la suerte es el 7'

result = re.findall('[0-9]+', text)
print(result)

timestamp = time.time()
local = time.localtime()
format = time.asctime(local)
formatted_date = time.strftime("%Y-%m-%d", local)
print(timestamp)
print(format)
print(formatted_date)

number =[1,1,2,1,2,1,4,5,3,3,21]

counter = collections.Counter(number)
print(counter)