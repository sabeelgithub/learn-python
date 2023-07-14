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
