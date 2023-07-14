





# destructor
class Myclass:
    def __init__(self):
       self.name = 'sabeel'
    
    def __del__(self):
        print('cleaned up everything')


    def Name(self):
        print(self.name)

obj = Myclass()
obj.Name()
 

# end




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

# destructor and constructor
class A:
    def __init__(self):
        print('started')
    def __del__(self):
        print('end')

a = A()
        
# end

# class and object
class computer:
    relation = 'love'
    def __init__(self,name,age):
        self.name = name
        self.age = age
  

    def compare(self,other):
        if self.age == other.age:
            print('they are same ')
        else:
            print('they are different')       
        
    

com1 = computer('sabeel',22)
com2 = computer('anshi',20)
com2.age = 22
com1.compare(com2)
computer.relation = 'partners'
print(com1.name,com1.age,com1.relation)
print(com2.name,com2.age,com2.relation)
# end

# type of mthods
class students:
    school = 'govt arts and science college kondotty'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3 

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def info(cls):
        print(cls.school) 
    
    @staticmethod
    def attension():
        print('every one get ready for assembly')
    
       
s1 = students(54,38,24)
s2 = students(23,45,67) 
s1.m1 = 10       
print(s1.avg())
print(s2.avg())
students.info() 
students.attension()
# end types of method

# inner class starts
class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()
    
    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Mac'
            self.ram = 8 
            self.cpu = 'i5'

        def show(self):
            print(self.brand,self.ram,self.cpu)   


s1 = Students('sabeel',22)
s2 = Students('anshida',20)

s1.show()
s2.show()



# polyphorpism

# duck typing 


class VScode:
    def exicute(self):
        print('cheking')
        print('reading')
        print('combiling')
        print('running')

class Laptop:
    def code(self,IDE):
        IDE.exicute()


IDE = VScode()
obj = Laptop()
obj.code(IDE)

#  end duck typing


# operator overloading


a=5
b=6
print(a-b)
print(int.__sub__(a,b))

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1+other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3  
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1>r2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
        
        

s1 = student(40,69)
s2 = student(60,65)
s3=s1+s2   
print(s3.m1,s3.m2)    

        
if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
         

a=5
print(a.__str__())
print(s1)

# end operator overloading

# method overloading

class A:
    def sum(self,a=None,b=None,c=None):
        s=0 
        if a!=None and b!=None and c!=None:
           s = a + b + c
        elif a!=None and b!=None:
            s= a + b
        else:
            s = a 

        return s     
       
        
a1 = A()

print(a1.sum(1))
        
# end method overloading

# method over riding
class A:
    def show(self):
        print('in show A')

class B(A):
    def show(self):
        print("in show B")
        
         


obj = B()
obj.show()

# method over riding end


# exception 
a = 5
b = 2

try:
    print('opened resource')
    print(a/b)
    k= int(input('enter a number:'))
    print(k)
   
    
except ZeroDivisionError as e:
   
    print('divisio by zero not possible',e)
except ValueError as e:
    print('invalid input')
except Exception as e:
    print(e)
    
finally:
    print('closed resource')


print('byeeeee')
# exception end

# multi threading
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)



t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()

print(current_thread())
print('end')

# multi threading end

# encapsilation

class car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color

    def perfomance(self):
            print('the car has speed {} and color {}'.format(self.__speed,self.__color))

    def set_speed(self,value):
         self.__speed = value   

    def get_speed(self):
           return self.__speed

    def set_color(self,value):
         self.__color = value   

    def get_color(self):
           return self.__color   
        
car1 = car(300,'blue')  
print(car1.get_speed(),car1.get_color()) 
car1.set_color('green')
car1.set_speed(400)  
car1.perfomance()

# end encapsilation



# abstract class
from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def sides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def sides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def sides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def sides(self):
        print("I have 6 sides")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def sides(self):
        print("I have 4 sides")
 
# Driver code
R = Triangle()
R.sides()
 
K = Quadrilateral()
K.sides()
 
R = Pentagon()
R.sides()
 
K = Hexagon()
K.sides()
# end abstact class

# user input
name = input('enter your name:')
email = input('enet your email:')
print(name,email)

num1 = int(input('enter number 1:')) 
num2 = int(input('enter number 2:'))
print(num1+num2)

num3 = float(input('enter number 1:')) 
num4 = float(input('enter number 2:'))
print(num3+num4)
# user input end


# file handling 
f = open('C:/Users/Lenovo/Desktop/sabeel.txt', 'a' )
f.write('miss you more\n')
f.close()

f = open('C:/Users/Lenovo/Desktop/sabeel.txt', 'r' )
read = f.read()
print(read)
f.close()
# file handling end


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




########################### ENCAPSILATION ####################################
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # protected attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


# Creating an instance of BankAccount
account = BankAccount("1234567890", 1000)

# Accessing protected attribute (conventionally considered protected)
print("Account Number:", account.get_account_number())

# Accessing private attribute (name mangling is applied)
# This will result in an AttributeError
# print("Balance:", account.__balance)

# Depositing and withdrawing money
account.deposit(500)
account.withdraw(200)

# Accessing balance through a getter method
print("Balance:", account.get_balance())


########################### END ENCAPSILATION ####################################

########################### ABSTRACTION ##############################
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Creating instances of Rectangle and Circle
rectangle = Rectangle(5, 3)
circle = Circle(7)

# Calling abstract methods through the objects
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

########################### END ABSTRACTION ##############################







      
    
 


     
         
