# single inheritence

class A:
    def feature1(self):
        print("feature 01 working")

class B(A):
    def feature2(self):
        print("feature 02 working")

b = B()
b.feature1()
b.feature2()

#  end single inheritence

# multilevel inheritence  
      
class A:
    def feature1(self):
        print("feature 01 working")

class B(A):
    def feature2(self):
        print("feature 02 working")

class C(B):
    def feature3(self):
        print("feature 03 working")

c = C()
c.feature1()
c.feature2()
c.feature3()
 

#  end multilevel inheritence  


# multiple inheritance
# eg 1

class A:
    def feature1(self):
        print("feature 01 working")

class B():
    def feature2(self):
        print("feature 02 working")

class C(A,B):
    def feature3(self):
        print("feature 03 working")

c = C()
c.feature1()
c.feature2()
c.feature3()


# eg 2

class A:
    def __init__(self):
        print("in A")

    def feature1(self):
        print("feature 01 working")
    
    def feature(self):
        print("featue A working")

class B():
    def __init__(self):
        print("in B")

    def feature2(self):
        print("feature 02 working")
    
    def feature(self):
        print("feature B working")

class C(B,A):
    def __init__(self):
        print("in C")
        super().__init__()

    def feature3(self):
        print("feature 03 working")

    def feature(self):
        return super().feature()

c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature()


# end multiple inheritence