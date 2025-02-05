from functools import reduce

li = [1,2,3,4,5]
product = reduce(lambda x,y : x*y,li)
print(product)

ti = [1,2,3]
add = reduce(lambda x,y: x+y,ti,10)
print(add)