 # duck typing 

class Dog:
    def speak(self):
        print("Bow Bow")

class Cat:
    def speak(self):
        print("Meow Meow")

def animal_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)

#  end duck typing

# method overriding

class A:
    def show(self):
        print('in show A')

class B(A): 
    def show(self):
        print("in show B")
     
                
obj = B()
obj.show()

# method overriding end

# method overloading

class MathOperations:
    def add(self,*args):
        total = 0
        for value in args:
            total += value
        return print(total)

m = MathOperations()
m.add(5,2,3)

# method overloading end

# operator overloading

class Maths:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return print(self.x+other.x)
    
    def __sub__(self,other):
        return print(self.y-other.y)
    
    def __mul__(self,other):
        return print(self.x*other.x)
    

m1 = Maths(1,2)
m2 = Maths(3,4)

m1+m2
m1-m2
m1*m2

# operator overloading end

        
        