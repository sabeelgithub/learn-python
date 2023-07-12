########### PACKING AND UNPACKING ##########
# Packing into a tuple
packed = (1, 2, 3)  
print(packed)
# unpacking
a,b,c = packed
print(a)
print(b)
print(c)

my_list = ['ba', 'con', 'sol']
print(my_list)
d,e,f = my_list
print(d)
print(e)
print(f)

my_dict = {'name': 'John', 'age': 25}
name, age = my_dict  # Unpacking keys from a dictionary
print(name)  # Output: 'name'
print(age)

my_set = {2,3,4}
print(my_set)
ab,bb,cd = my_set
print(ab)
print(bb)
print(cd)


########### END PACKING AND UNPACKING #############