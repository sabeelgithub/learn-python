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

        