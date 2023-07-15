# min
print(min(1,2,3,4,5))
# max
print(max(1,2,3,4,5))
# pow
print(pow(2,3))

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


while True:
    name = input("Enter a name (or 'quit' to exit): ")
    if name == 'quit':
        break
    print("Hello,", name)












# custom exception
class InvalidAgeError(Exception):
    def __init__(self,value):
        self.value = value

try:
    age = int(input('how old are you:'))
    if age < 0 or age >= 120:
        raise InvalidAgeError('sorry ,the age doesn\'t support')
    print(f'you ar {age}year old')
except ValueError:
    print('invalid integer was entered')
except InvalidAgeError as e:
    print(e)

# end
        
        

  



















# iterator
class Topten:
    def __init__(self,start,limit):
        self.start = start
        self.limit = limit

    def __iter__(self):
        
        return self    
    
    def __next__(self):
       
        if self.start<= self.limit:
         val = self.start
         self.start += 1
         return val
        else:
            raise StopIteration
    
values = Topten(1,20)
print(next(values))
print(values.__next__())
for i in values:
    print(i)


# eg 1
nums = [7,8,9,5]

it = iter(nums)
print(it.__next__())
print(it.__next__())

print(next(it))
for i in it:
    print(i)
# end

# eg 2
string = "GFG"
ch_iterator = iter(string) 
print(next(ch_iterator))
print(next(ch_iterator))
for i in ch_iterator:
    print(i)
# end    


# end iterator

# generator
def topTen():
    n=1
    while n <=10:
        sq = n*n
        yield sq
        n +=1


values = topTen()   
print(values.__next__()) 
for i in values:
    print(i)

def topTen(start,limit):
    n=start
    while n <=limit:
        sq = n*n
        yield sq
        n +=1


values = topTen(1,10)   
print(values.__next__()) 
for i in values:
    print(i)    

# end

# decorators

def div(a,b):
    print(a/b)


def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)  
    return inner

div = smart_div(div)
div(2,4)  

# end

# first class object
# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()

print(shout('hello'))

yell = shout

print(yell('sabeel'))

# passing the function as an argument
#Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)


# Returning functions from another function
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))
# end
















# about meta class attributes

class MyClass:
    class Meta:
        pass

print(MyClass.Meta.__name__)

class BaseClass:
    pass

class MyClass(BaseClass):
    class Meta:
        pass

top = MyClass.Meta.__bases__
for i in top:
    print(i.__name__)
print(MyClass.Meta.__bases__)

class MyClass:
    class Meta:
        my_attribute = 'Hello, world!'

print(MyClass.Meta.__dict__)

class MyClass:
    class Meta:
        pass

print(MyClass.Meta.__module__)



# end meta class attributes



# random module  and its methods in python = for generating random numbers
import random

# random() - provide a floating point between 0-1,inclusive of zero and exclusive of 1
a = random.random()
print(a)

# randint(a,b) - return random integer in which both a and b is included
b = random.randint(1,100)
print(b)

# uniform(a,b) - return random float in which a included and b excluded
c = random.uniform(-10,-1)
d = random.uniform(100,200)
print(c)
print(d)

# choice() - it will return a random number from our input/list ,tuple,integer are support
e = random.choice([1,2,3,4,5])
print(e)

f = random.choice('helllooooo')
print(f)

# shuffle() - it will suffle our items
l = [1,2,3,4,5]
random.shuffle(l)
print(l)

from array import *
l = array('i',[1,2,3,4,5])
random.shuffle(l)
print(l)
# random module and method end


# finding sum of n numbers

def sumAll(n):
    print(sum(range(1,n+1)))
    return

sumAll(10)

# end

# creating dictionary using list comprehension

dictt = {i:i+2 for i in range(1,11)}
print(dictt) 

# end


# Creating a string  
sequence = 'abjucujba'  
# Reversing the string  
reverse = sequence[::-1]  
  
# Checking if the string is a palindrome  
if reverse == sequence:  
    print("The sequence is a palindrome")  
else:  
    print("The sequence is not a palindrome")











      
    
 


     
         
