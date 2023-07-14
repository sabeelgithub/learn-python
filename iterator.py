########## iterator #############

list = [1,2,3,4,5,6,7]
it = iter(list)
print(it)
print(next(it))
print(it.__next__())
for i in it:
    print(i)


class TopTen:
    def __init__(self):
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
    
top = TopTen()
print(top.__next__())
print(next(top))

for i in top:
    print(i)
       

########### end ##################