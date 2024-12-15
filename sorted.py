###########  sorted() ###########

# sorted() method retun a list after sorting ascending or descending order,can be sort iterables
var = [1,5,9,0,6,5]
res = sorted(var)
print(res)

# in decreasing order
print(sorted(var,reverse=True))

tu = ('d','cg','a','b')
sorted_tu = sorted(tu,key=None,reverse=False)
print(sorted_tu)

######### end ###############