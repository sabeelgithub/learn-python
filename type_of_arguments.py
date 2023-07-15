# positional argument
def greet(name, age):
    print("Hello", name, "you are", age, "years old.")

greet("Alice", 25)
# end

# key-value
def greet(name, age):
    print("Hello", name, "you are", age, "years old.")

greet(age=30, name="Bob")
# end

# default
def greet(name, age=18):
    print("Hello", name, "you are", age, "years old.")

greet("Charlie")  # age defaults to 18
greet(age=27,name="David", )  # age is overridden with 27
greet("David",27 )  # age is overridden with 27
# end

# variable length

# *args
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
my_function("apple", "banana", "orange")

# end

# **kwargs
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name="Alice", age=25)
my_function(city="New York", country="USA")

# end

# combination
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

my_function(1, 2, 3, name="Alice", age=25)

# end

# end


