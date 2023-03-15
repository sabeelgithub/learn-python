# zip function
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a,b)
#print(list(x))
# we can use list ,tuple ,set as well as dictionary also
# we can iterate over it
for (a,b) in x:
    print(a,b)
   
# end zip function


# function
def square(a):
    return  a * a
result = square(5)
print(result)

# lambda function
fun = lambda a,b:a + b

result = fun(6,7)
print(result)

# lambda function
fun = lambda a:a * a

result = fun(6)
print(result)

from functools import reduce
# lambda inside filter method
nums = [1,2,3,4,5,6,7,8]
print(nums)
evens = list(filter(lambda n:n%2==0,nums))
print(evens)

# lamba inside map method
double = list(map(lambda n:2*n,evens))
print(double)


# lambda inside reduce method
sum = reduce(lambda a,b:a+b,double)
print(sum)
# end


# list comprehension
list = ['apple','grape','watermelon','banana']
newlist = []

for i in list:
    newlist.append(i)

print(newlist)    

aginlist = [x for x in list if x == 'apple']
print(aginlist)

solist  = [x for x in list if x != 'apple']
print(solist)

top = [x for x in list if 'b' in x]
print(top)

# end
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


# frozen set
thisSet = {'a','e','i','o','u'} 
frozenSet = frozenset(thisSet)
print(frozenSet)

thisList = ['a','e','i','o','u']
frozenSet1 = frozenset(thisList)
print(frozenSet1)

thisTuple = ('a','e','i','o','u')
frozenSet2 = frozenset(thisTuple)
print(frozenSet2)

thisDict = {'one':1,'two':2,'three':3}
frozenSet3 = frozenset(thisDict)
print(frozenSet3)

thisString = 'anshida'
frozenSet4 = frozenset(thisString)
print(frozenSet4)

unionFrozen = frozenSet.union(frozenSet4)
print(unionFrozen)

interFrozen = frozenSet.intersection(frozenSet4)
print(interFrozen)

symFrozen = frozenSet.symmetric_difference(frozenSet4)
print(symFrozen)

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
        
        
# type casting
x = float(1)   # x will be 1
y = float(2.8) # y will be 2
z = float("3") # z will befloat
print(x,y,z)
# end
  


# list
thislist = list(('hlo','hot','koi'))
print(thislist)
print(thislist[0:2]) 
print(thislist[-3:-1])
thislist[0] = 6
print(thislist)
del thislist[0]
print(thislist)
thislist.append('bossee')
print(thislist)
thislist.insert(0,'anshidaa')
print(thislist)
thislist.extend(('sebi','anshu','pottathyee','mandathyeee'))
print(thislist)
seb = {'ann':1,'konn':2}
thislist.remove('hot')
print(thislist)
thislist.pop()
print(thislist)
thislist.reverse()
print(thislist)
thislist.sort()
print(thislist)
thislist.extend(seb)
print(thislist)
thislist.sort(reverse=True)
print(thislist)
againList = thislist.copy()
print(againList)
ann = ['nee','njn']
print(ann*3)
print(ann+thislist)
lol = [1,2,3,4]
lol.clear()
print(lol)
for i in thislist :
    print(i)

newList = []
for i in thislist:
    newList.append(i)
print(newList)

againNew = [i for i in thislist if  'a' in i]
print(againNew)

molu = ['lo','koi','hm']
molu[1:2] = ['ann','konn']
print(molu)
# end


# tuple
thisTuple = tuple(('lo',1,False,'ann'))
print(thisTuple)
print(thisTuple[0])
print(thisTuple[0:3])
print(thisTuple[-3:-1])
thisSet = list(thisTuple)
print(thisSet)
thisSet.append('moloos')
print(thisSet)
thisTuple = tuple(thisSet)
print(thisTuple)
# end


# set
thisSet = set(('lo','lo',1,'koi','molu'))
print(thisSet)
for i in thisSet:
    print(i)
thisSet.remove(1)
print(thisSet)    
thisSet.discard('lo')
print(thisSet)
thisSet.add('lo')
print(thisSet)
set = {'molloos'}
thisSet.update(set)
print(thisSet)
set.clear()
print(set)
setNew = {'nasf','andi','arif','mthy','piri','vellu','das'}
unionSet = thisSet.union(setNew)
againNew = {'nasf','andi','arif','mthy','piri','vellu','das','lo',1,'koi','molu'}

print(unionSet)
setNew.symmetric_difference_update(againNew)
print(setNew)

pinnim = {'nasf','andi','arif','mthy','piri','vellu','das'}
pinnimPinnim = {'nasf','andi','arif','mthy','piri','vellu','das','lo',1,'koi','molu'}
pinnim.intersection_update(pinnimPinnim)
print(pinnim)
# end

# dictionary
thisDict = dict(one = 1,two = 'two',three=3)
print(thisDict)
print(thisDict['one'])
top = thisDict.get('three')
print(top)
print(thisDict.keys())
print(thisDict.values())
print(thisDict.items())
print(thisDict)
thisDict.update({'two':2})
print(thisDict)
thisDict.update({'four':'four'})
print(thisDict)
thisDict.popitem()
print(thisDict)
thisDict.pop('three')
print(thisDict)

nestedDict = {
    'child1':{
    'name':'muhammed',
    'age':2
    },
    'child2':{
    'name':'fathima',
    'age':4
    }

}
print(nestedDict)




child1={
    'name':'anshu',
    'age':20
}
child2 = {
    'name':'sebi',
    'age':22
}
pinnim = {
    'child1':child1,
    'child2':child2,
    
}
print(pinnim)
# end

# join method

myList = ["John", "Peter", "Vicky"]

x = '#'.join(myList)

print(x)

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

# inner class ends


# single inheritence
class A:
    def feature1(self):
        print("fea 1 is working")

a1 = A()
a1.feature1()

class B(A):
    def feature2(self):
        print("fea 2 is working")

b1 = B()
b1.feature1()
b1.feature2()

#  end single inheritence

# multilevel inheritence  
      
class A:
    def feature1(self):
        print("fea 1 is working")

a1 = A()
a1.feature1()

class B(A):
    def feature2(self):
        print("fea 2 is working")

b1 = B()
b1.feature1()
b1.feature2()

class C(B):
    def feature3(self):
        print('fea 3 is working')

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()    

#  end multilevel inheritence  

# multiple inheritence  
class A:
    def feature1(self):
        print("fea 1 is working")

a1 = A()
a1.feature1()

class B:
    def feature2(self):
        print("fea 2 is working")

b1 = B()
b1.feature2()

class C(A,B):
    def feature3(self):
        print('fea 3 is working')

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()

# end multiple inheritence

# constructor multiple inheritence


class A:
    def __init__(self):
        print('in init A')
    def feature1(self):
        print("fea 1 is working")

    def feature2(self):
        print("fea 2-A is working")   

class B:
    
    def __init__(self):
        print('in init B')
        

    def feature2(self):
        print("fea 2-B is working")
    
    def feature3(self):
        print("fea 3 is working") 

class C(A,B):
    def __init__(self):
        super().__init__()
        print('in int c')

    def fea(self):
        super().feature2()

obj = C()
obj.fea()

#  end constructor multiple inheritence

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






      
    
 


     
         
