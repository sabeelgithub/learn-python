# Create a dictionary of squares using dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}

print(squared_dict)

# Create a dictionary of even squares using dictionary comprehension with a condition
numbers = [1, 2, 3, 4, 5]
even_squared_dict = {num: num**2 for num in numbers if num % 2 == 0}

print(even_squared_dict)


string = 'sabeel'
dict = {i:i for i in string if i == 'e' }
print(dict)