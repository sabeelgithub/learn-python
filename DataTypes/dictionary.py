################# DICTIONARY ##################

# dict()
# dict can be created using dict constructor
thisDict = dict(one = 1,two = 'two',three=3)
print(thisDict)

# dict canot be acces with index,but we can access with key
print(thisDict['one'])

# also with get()
print(thisDict.get('three'))

# keys()
# for getting keys of the dictionary
print(thisDict.keys())

# values()
# for getting values of the dictionary
print(thisDict.values())

# items()
# for getting items of the dictionary
print(thisDict.items())

# update()
# for updating the dictionary
thisDict.update({'two':2})
print(thisDict)
thisDict.update({'four':4})
print(thisDict)

# popitem()
# for removing the last item of the dictionary
thisDict.popitem()
print(thisDict)

# copy()
# for copying the dictionary
newDict = thisDict.copy()
print(newDict)

# pop()
# for removing the specified key
newDict.pop('three')
print(newDict)

# del keyword is used for deleting the elements in the dictionary
del thisDict['two']
print(thisDict)

# clear()
# it removes all the elements from the dictionary
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


# nested dictionary
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