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
        print('in int c')
        super().__init__()

    def fea(self):
        super().feature2()
        

obj = C()
obj.fea()