############# TUPLE ###############
thisTuple = tuple(('lo',1,False,'ann'))
print(thisTuple)
print(thisTuple[0])
print(thisTuple[:])
print(thisTuple[0:])
print(thisTuple[0:3])
print(thisTuple[-3:-1])
print(thisTuple[-3:])

# in to list
thisList = list(thisTuple)
print(thisList)
thisList.append('ann')
thisTuple = tuple(thisList)
print(thisTuple)

# in to set
into_set = set(thisTuple)
print(into_set)

tp1 = ('wq',1,True,None)
tp2 = ('d','w')
print(tp1+tp2)
print(tp1*3)
############ END #################
