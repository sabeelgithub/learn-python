from array import *
# # (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.3,4.5,3.5])
print(arr1)
print(arr2)
print(type(arr1[1]))
print(arr1[::-1])

arr1.append(7)
print(arr1)

arr1.insert(7,8)
print(arr1)

arr1.insert(0,0)
print(arr1)

arr1.extend([9,10])
print(arr1)
print(arr1[0])

arr1.remove(10)
print(arr1)

arr1.pop()
print(arr1)
arr1.pop(2)
print(arr1)

arr1.fromlist([100,101])
print(arr1)


print(arr1.tolist())   
l = [5,6,7]

def traverse_array(arr):
    for i in arr:
        print(i)

traverse_array(arr1)

# accessing
"""
Q - access value in a specified index
"""
def accessElement(arr,index):
    if index >= len(arr):
        print("out of index")
    else:
        print(arr[index])

accessElement(arr1,9)

