increment = lambda x: x+1
high = lambda x, func: x + func(x)

result = high(2, increment)
result2 = high(2, lambda x: x+2)
result3 = high(2, lambda x: x*5)
print(result)
print(result2)
print(result3)