############## ZIP METHOD ##############
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a,b)
print(x)
# print(list(x))
# print(tuple(x))
# print(set(x))
# print(dict(x))
for i in x:
    print(i)

# example 2
numbers = [1, 2, 3]
letters = 'sabeel'
zipped = zip(numbers, letters)

for item in zipped:
    print(item)



############## END #################### 