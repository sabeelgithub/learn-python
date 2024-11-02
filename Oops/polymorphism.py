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

# method over riding
class A:
    def show(self):
        print('in show A')

class B(A): 
    def show(self):
        print("in show B")
     
                
obj = B()
obj.show()
# end

# duck typing



class Animal:
    def perform(self):
        print('behave like animal')

class Human:
    def perform(self):
        print('humam is behaving')

class Circus:
    def play(self,animal:Animal):
        animal.perform()
        # print(f'some one behaving')


a = Animal()
b = Human()
c = Circus()
c.play(b)

# end


# operator overloading

class A:
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def __add__(self,b):
        print(self.name+' '+b.name)

a = A('sabeel','ovr')
b = A('ann','thani')
a + b   

# end

# method overloading
class C:
    # def sum(self,a,b):
    #     print(a+b)
    def sum(self,*args):
        total = 0
        for i in args:
            total += i
        print(total)

c = C()
c.sum(1,2,6,6,89)

# end
        
        