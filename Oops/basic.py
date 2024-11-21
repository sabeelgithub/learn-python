# simple implementation

class TestClass:
    def welcome(self):
        print("welcome to test class")


test1 = TestClass()
test1.welcome()
TestClass.welcome(test1)

# end simple implementation

# types of variables

class Love:
    relationship_status = "Married" # class variable

    def __init__(self,name,age):
        self.name = name   # instance variable
        self.age = age     # instance variable

    highlight = "Love" # class variable
    

wife = Love("Anshida",22)
husbend = Love("Sabeel",23)
print(wife.name,wife.age,wife.relationship_status,wife.highlight)
print(husbend.name,husbend.age,husbend.relationship_status,husbend.highlight)
print(Love.relationship_status,Love.highlight)

# end types of variable

# types of methods

class Student:
    school = "HIOHSS Olavattur"
    def __init__(self,name,mark1,mark2,mark3):
        self.name = name
        self.biology = mark1
        self.maths = mark2
        self.physics = mark3

    def average_mark(self):
        average = (self.biology + self.maths + self.physics)/3
        print(f"Average Mark of {self.name} is : {average}")

    @classmethod
    def school_name(cls):
        print(f"School is {cls.school}")

    @staticmethod
    def assembly():
        print("Every Get Ready For Assembly")



s1 = Student("Abu",12,13,14)
print(s1.name,s1.biology,s1.maths,s1.physics,s1.school)
s1.average_mark()
s1.school_name()
s1.assembly()
Student.school_name()
Student.assembly()

# end types of methods

# inner class

class Student:
    def __init__(self,name,model,ram,ssd):
        self.name = name
        self.lap = self.Laptop(model,ram,ssd)  # object defined inside of the outer class
    
    def student(self):
        print(f"Student is {self.name}")
        self.lap.system()

    class Laptop:
        def __init__(self,model,ram,ssd):
            self.model = model
            self.ram = ram
            self.ssd = ssd
        
        def system(self):
            print(f"system is {self.model}-{self.ram}-{self.ssd}")



s1 = Student("Abu","Mac",512,8)
print(s1.name)
s1.student()

# object is defined outside of the outer class
l1 = s1.Laptop("Windows",16,1)
l1.system()

# end inner class


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

# end destructor
        

        