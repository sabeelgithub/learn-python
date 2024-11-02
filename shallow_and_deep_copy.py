# assingment operator (=)

list1 = [1,2,3,4]
list2 = list1
print(list1,list2)
list2[3]=9
print(list1,list2)

# Here both variable are referencing to the same object,changes made to the list1 will be reflected in list2 and vice verca

import copy

# Original list
original_list = [[1, 2, 3], [4, 5, 6]]
print(original_list,'1')

# Shallow copy
shallow_copy = copy.copy(original_list)
print(shallow_copy,'2')  

# Deep copy
deep_copy = copy.deepcopy(original_list)
print(deep_copy,'3') 

# Modify the nested list in shallow copy
shallow_copy[0][0] = 9
print(shallow_copy,'sh')
print(original_list,'og')

# Modify the nested list in deep copy
deep_copy[1][0] = 8


print(deep_copy,'6')      
print(original_list,'4')      

'''
in the case shallow copy it create a new object and references the nested object,but in the case of deep copy it create
a new  object and recuirsevely copy all nested object also.

that means in the case of shallow copy changes made to the mutable nested object effect original object also,vice versa
but in the case deep copy changes made to the mutable nested object will not effect the original object,vice verca
'''

