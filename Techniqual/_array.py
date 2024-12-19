"""
Q - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

# ans-1

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


sol  = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([3,2,4],6))
print(sol.twoSum([3,3],6))


# ans-2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Dictionary to store number and its index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:  # Check if the complement exists in the dictionary
                return [num_to_index[complement], i]  # Return indices of the complement and current number
            num_to_index[num] = i  # Store the number with its index for future lookups

sol  = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([3,2,4],6))
print(sol.twoSum([3,3],6))



"""
Q-linear search and binary search
"""

# ans
class Solution:
    def linearSearch(self,arr:list,target:int) -> int:
        for idx,i in enumerate(arr):
            if i == target:
                return idx + 1
        return -1
    
    def binarySearch(self,arr:list,target:int):
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid + 1
            if target < arr[mid]:
                end = mid-1
            if target > arr[mid]:
                start = mid + 1
        return -1
    

    
sol = Solution()
target = 10
li = sol.linearSearch([2,4,1,5,6,8],target)
if li == -1:
    print(f"{target} is not found in the list")
else:
    print(f"{target} is found in {li} position")

bi = sol.binarySearch([1,2,3,4,5,6,7,8,9,10],target)
if bi == -1:
    print(f"{target} is not found in the list")
else:
    print(f"{target} is found in {bi} position")


"""
Q-Given two numbers  and .  indicates the number of elements in the array  and  indicates number of queries. You need to perform two types of queries on the array .

You are given  queries. Queries can be of two types, type 1 and type 2.

Type 1 queries are represented as 1 i j : Modify the given array by removing elements from  to  and adding them to the front.

Type 2 queries are represented as 2 i j : Modify the given array by removing elements from  to  and adding them to the back.

Your task is to simply print  of the resulting array after the execution of  queries followed by the resulting array.

Note While adding at back or front the order of elements is preserved.

Input Format

First line consists of two space-separated integers,  and .
Second line contains  integers, which represent the elements of the array.
 queries follow. Each line contains a query of either type 1 or type 2 in the form 

Constraints



Output Format

Print the absolute value i.e.  in the first line.
Print elements of the resulting array in the second line. Each element should be seperated by a single space.

Sample Input

8 4
1 2 3 4 5 6 7 8
1 2 4
2 3 5
1 4 7
2 1 4
Sample Output

1
2 3 6 5 7 8 4 1

"""

# ans-1
from typing import List

def looping(sl_arr,arr):
    for i in sl_arr:
        arr.remove(i)
    return arr

def execution(N:int,M:int,arr:List[int],queries:List[str]):
   
    for query in queries:
        if query[0] == '1':
            sl_arr = arr[int(query[1])-1:int(query[2])]
            arr = looping(sl_arr,arr)
            arr = sl_arr + arr
        elif query[0] == '2':
            sl_arr = arr[int(query[1])-1:int(query[2])]
            arr = looping(sl_arr,arr)
            arr = arr + sl_arr
            
    diff = arr[0]-arr[len(arr)-1]
    diff = abs(diff)
    return diff,arr
    
diff,final_arr = execution(8,4,[1,2,3,4,5,6,7,8],['124','235','147','214'])
print(diff)
for i in final_arr:
    print(i,end=" ")
            
# ans-2

n = int(input("Enter length of array:"))
arr = [i for i in range(1,n+1)]
print(f"Your array is : {arr}")
m = int(input("Enter number of queries:"))
queries = []
for i in range(1,m+1):
    query = input(f"Enter query {i}:")
    queries.append(query)

print(f"Your queries are : {queries}")

def execution(arr,queries):
    for query in queries:
        query_type,i,j = query
        query_type,i,j = int(query_type),int(i),int(j)
        i -= 1
        j -= 1

        if query_type == 1:
            arr = arr[i:j+1] + arr[:i] + arr[j+1:]
        elif query_type == 2:
            arr = arr[:i] + arr[j+1:] + arr[i:j+1]
        
    print(abs(arr[0] - arr[-1]))
    print(" ".join(map(str,arr)))

execution(arr,queries)


# accessing
from array import array


arr1 = array('i',[1,2,3,4,5,6])

"""
Q - access value in a specified index
"""
def accessElement(arr,index):
    if index >= len(arr):
        print("out of index")
    else:
        print(arr[index])

accessElement(arr1,9)


print("choices are,1 for int array,2 for float array")

try:
    choice = int(input('Enter choice you want:'))

    if choice == 1:
        length = int(input("Enter the length of array you want:"))
        arr = array('i',[])
        for i in range(length):
            num = int(input(f"Enter number {i+1}:"))
            arr.append(num)

    elif choice == 2:
        length = int(input("Enter the length of array you want:"))
        arr = array('d',[])
        for i in range(length):
            num = int(input(f"Enter number {i+1}:"))
            arr.append(num)
    
    print(arr)
except Exception as e:
    print(e)

"""
Q-search value
"""
def search_array_value(array,value):
    for idx,x in enumerate(array):
        if x == value:
            print(f"item found at {idx+1} position")
            break
    else:
        print("item not found")


search_array_value(arr1,101)


"""
Q - Find all paires in which thieir sum is 10
"""
arrk = array('i',[1,2,3,4,5,6,7,9])

values = []
for i in range(len(arrk)-1):
    for j in range(i+1,len(arrk)):
        if arrk[i] + arrk[j] == 10:
            values.append((arrk[i],arrk[j]))

if len(values) == 0:
    print("no such paries")
else:
    for i in values:
        print(i,',',end='')

"""
Q - Find first paires in which their sum is 10
"""
arrk = array('i',[1,2,3,4,5,6,7,9])
found = False
for i in range(len(arrk)-1):
    for j in range(i+1,len(arrk)):
        if arrk[i] + arrk[j] == 10:
            found = True
            print(f"Paires are {arrk[i]} and {arrk[j]}")
            break
    if found:
        break


if not found:
    print("paries not found")


"""
Q - reverse array
"""
arr = [1,4,5,7,3,2,5]

def reverese_array1(arr):
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    return print(arr)

reverese_array1(arr)

        