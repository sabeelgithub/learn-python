############## SET #################

thisSet = set(('lo','lo',1,'koi','molu'))
print(thisSet)
for i in thisSet:
    print(i)
# remove()
thisSet.remove(1)
print(thisSet) 
# discard()   
thisSet.discard('lo')
print(thisSet)

# add()
thisSet.add(True)
print(thisSet)
set1 = {'2','f'}
thisSet.update(set1)
thisSet.update([1,'fd',True])
thisSet.update((2,'erf'))
thisSet.update({'two':2,'erf':'erf'})
thisSet.update({'two':2,'erf':'erf'})
thisSet.update('iterable')

print(thisSet)
new = thisSet.copy()
print(new)
new.clear()
print(new)
del new

new1 = {1,2,3,'hj',True} 
union_new = thisSet.union(new1)
print(union_new)
print(thisSet)

newthis = thisSet
newly1 = thisSet.intersection(union_new)
print(newly1)
newthis.intersection_update(union_new)
print(newthis)

sym = thisSet.symmetric_difference(union_new)
print(sym)
newthis.symmetric_difference_update(union_new)
print(newthis)


############## END #################