############## SET #################
# set()
# set can be created using set constructor by passing iterables
thisSet = set(('lo','lo',1,'koi','molu'))
print(thisSet)

# set unindexed,so cant access with index and slicing
# we can access with for loop
for i in thisSet:
    print(i)

# remove()
# remove() will raise an exception if the value not found
thisSet.remove(1)
print(thisSet) 

# discard() 
# discard() will not raise an exception
thisSet.discard('lo')
print(thisSet)

# add()
# this method is using for adding an element to the set
thisSet.add(True)
print(thisSet)

# update()
# this method is using for adding iterables to the set
set1 = {'2','f'}
thisSet.update(set1)
thisSet.update([1,'fd',True])
thisSet.update((2,'erf'))
thisSet.update({'two':2,'erf':'erf'})
thisSet.update('iterable')
print(thisSet)

# copy()
# this method is using for copying the set
new = thisSet.copy()
print(new)

# clear()
# this method is using for clearing the set
new.clear()
print(new)

# del keyword is using for deleting the set
del new

# union()
# this method is using for union of two sets by a third set
new1 = {1,2,3,'hj',True} 
union_new = thisSet.union(new1)
print(union_new)
print(thisSet)

# intersection()
# this method is using for intersection of two sets by a third set
newthis = thisSet
newly1 = thisSet.intersection(union_new)
print(newly1)

# intersection_update()
# this method is using for making set commen element without creating a new set
newthis.intersection_update(union_new)
print(newthis)

# symmetric_difference()
# this method is using for making set in which only unique element are there by creating a new set
sym = thisSet.symmetric_difference(union_new)
print(sym)

# symmetric_difference_update()
# this method is using for making set in which only unique element are there without creating a new set
newthis.symmetric_difference_update(union_new)
print(newthis)

############## END #################