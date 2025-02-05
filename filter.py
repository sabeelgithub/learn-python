li = [1,2,3,4,5]
evens = filter(lambda x:x%2==0,li)
print(evens)
print(list(evens))

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x > 3, numbers)
print(list(result)) 