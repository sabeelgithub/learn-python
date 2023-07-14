class computer:
    relation = 'love'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def compare(self,other):
        if self.age == other.age:
            print('they are same')
        else:
            print('they are different')

com1 = computer('sabeel',22)
com2 = computer('anshida',20)
com2.age = 21
com1.compare(com2)
computer.relation = 'partners'
print(com1.name,com1.age,com1.relation)
print(com2.name,com2.age,com2.relation)

# types methods
class Students:
    college = 'Govt arts and science college kondotty'
    def __init__(self,m1,m2,m3):
        self.maths = m1
        self.bio = m2
        self.chem = m3
    
    def avg(self):
        print(f'average is {(self.maths+self.bio+self.chem)/3}')
        return
    @classmethod
    def info(cls):
        print(cls.college)
    
    @staticmethod
    def attension():
        print('every body get ready for assembly')


s1 = Students(10,40,45)
s2 = Students(35,50,40)
s1.maths = 35
s1.avg()
s2.avg()
Students.info()
Students.attension()

# end types of methos

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


# destructor
class Myclass:
    def __init__(self):
       print('started')
       self.name = 'sabeel'
    
    def __del__(self):
        print('cleaned up everything')


    def Name(self):
        print(self.name)

obj = Myclass()
obj.Name()
# end
        

        