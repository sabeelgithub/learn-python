################## FROZEN SET #############
# Actually frozenset is immutable version of set

# frozenset()
# frozenset can be created using frozenset constructor
thisSet = {'a','e','i','o','u'} 
frozenSet = frozenset(thisSet)
print(frozenSet)

thisList = ['a','e','i','o','u']
frozenSet1 = frozenset(thisList) 
print(frozenSet1)

thisTuple = ('a','e','i','o','u')
frozenSet2 = frozenset(thisTuple)
print(frozenSet2)

thisDict = {'one':1,'two':2,'three':3}
frozenSet3 = frozenset(thisDict)
print(frozenSet3)

thisString = 'anshida'
frozenSet4 = frozenset(thisString)
print(frozenSet4)

unionFrozen = frozenSet.union(frozenSet4)
print(unionFrozen)

interFrozen = frozenSet.intersection(frozenSet4)
print(interFrozen)

symFrozen = frozenSet.symmetric_difference(frozenSet4)
print(symFrozen)


################## END ####################
