############# LIST ################
thislist = list(('hlo','hot','koi'))
# list can be created with list constructor
print(thislist)

# accessing and slicing
print(thislist[0:2])
print(thislist[:2])
print(thislist[:])
print(thislist[0:])
print(thislist[-3:])
print(thislist[-3:-1])

# assigning
thislist[0] = 6
print(thislist)

# append()
# element can be added at the end using append()
thislist.append(9)
thislist.append(True)
thislist.append(None)
thislist.append('boss')
print(thislist)

# insert() 
# element can be added at the specified index using insert()
thislist.insert(0,8)
thislist.insert(1,False)
thislist.insert(2,None)
thislist.insert(4,'sabi')
print(thislist)

# extend()
# iterable can be added at the end using extend()
thislist.extend(('anshu','pottathyee',6))
thislist.extend(['anshu','pottathyee',6])
thislist.extend({'anshu','pottathyee',6})
thislist.extend({'name':'sabeel','age':22})
thislist.extend('iterable')
print(thislist)

# remove()
# element can be removed using remove() by specifying element
thislist.remove('name')
thislist.remove('age')
thislist.remove(False)
thislist.remove(True)
print(thislist)

# pop()
# element can be removed using pop() by specifying index
thislist.pop() # by default it removes the last element
thislist.pop(0)

# process of removing all the integers from the list
thislist = [i for i in thislist if not isinstance(i,int)]

# sort()
# element can be sorted using sort() in alphanumeric order
# this only work in the case of list having same type of element
# list with different type of element can't be sorted
# by default it sorts in ascending order,user reverse=True to sort in descending order
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

# reverse()
# element can be reversed using reverse()
thislist.reverse()
print(thislist)


# index()  
# it returns the index number specified value
list1 = [1,2,3,4,5,6,'one']
print(list1.index('one'))

# count()
# it returns the number of specified value
listm = [1,1,2,3,4]
print(listm.count(1))

# sum()
# it returns the sum of all the elements
# It can be applied only on number iterables
print(sum(listm))

# max() and min()
# it returns the maximum and minimum value
# It can be applied only on number iterables
l = [1,2,3,4,5,6,7]
print(max(l))
print(min(l))

# conver all elements of the list to string using list comprehension
list1 = [1,2,3,4,5]
list1 = [str(i) for i in list1]
print(list1)

# list comprehension
# process of creating a new list from an existing list
list = ['apple','grape','watermelon','banana']
newlist = []

for i in list:
    newlist.append(i)

print(newlist)    

aginlist = [x for x in list if x == 'apple']
print(aginlist)

solist  = [x for x in list if x != 'apple']
print(solist)

top = [x for x in list if 'b' in x]
print(top)

# copy()
# it returns a copy of the list
print(thislist)
new = thislist.copy()
print(new)

# del keyword is using for deleting an element from the list
del thislist[0]
del thislist[1]
del thislist[2]
del thislist[3]
del thislist[4]
print(thislist)

# clear()
# it removes all the elements from the list,but the list remains there with empty
thislist.clear()
print(thislist)

setnew1 = [1,3,'one',True]
setnew2 = [1,3,'one',True]

# list can be added using + operator
setnew = setnew1 + setnew2
print(setnew)

# list can be multiplied using * operator
setnew = setnew1 * 3
print(setnew)

# in to tuple
into_tuple = tuple(setnew1)
print(into_tuple)

# in to set
into_set = set(setnew2)
print(into_set)

# join()
# it joins iterables in to a string

myList = ["John", "Peter", "Vicky"]
x = ' '.join(myList)
print(x)


################ END LIST #################







