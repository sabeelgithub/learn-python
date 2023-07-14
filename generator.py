############# GENERATOR ##############
def TopTen():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1

a = TopTen()
print(a)
print(a.__next__())
print(next(a))
for i in a:
    print(i)

############## END ###################
