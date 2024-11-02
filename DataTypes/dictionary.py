################# DICTIONARY ##################

thisDict = dict(one = 1,two = 'two',three=3)
print(thisDict)
print(thisDict['one'])
print(thisDict.get('three'))
print(thisDict.keys())
print(thisDict.values())
print(thisDict.items())
thisDict.update({'two':2})
print(thisDict)
thisDict.update({'four':4})
print(thisDict)
thisDict.popitem()
print(thisDict)
newDict = thisDict.copy()
print(newDict)
newDict.pop('three')
print(newDict)
del thisDict['two']
print(thisDict)
newDict.clear()
print(newDict)

dict1 = {'one':1,'two':2,'three':'3'}
# converting dict in list
listDict = list(dict1)
print(listDict)

# converting dict in to tuple
tupleDict = tuple(dict1)
print(tupleDict)

# coverting dict in set
setDict = set(dict1)
print(setDict)

nestedDict = {
    'child1':{
    'name':'muhammed',
    'age':2
    },
    'child2':{
    'name':'fathima',
    'age':4
    }

}
print(nestedDict)




child1={
    'name':'anshu',
    'age':20
}
child2 = {
    'name':'sebi',
    'age':22
}
pinnim = {
    'child1':child1,
    'child2':child2,
    
}
print(pinnim)


################# END #########################