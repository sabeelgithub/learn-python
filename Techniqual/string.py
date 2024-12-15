# Q - Write a pogramme to count occurance of each word in a string

# ans1
def word_count(str):
    str_list = str.split()
    count_dict = {}
    for item in str_list:
        if item not in count_dict.keys():
            count_dict[item] = 1
        else:
            count_dict[item] += 1

    return print(count_dict)

# word_count("hello world hello koi world world")

# ans 2
from collections import Counter

def word_count(str):
    str_list = str.split()
    return print(Counter(str_list))

# word_count("hello world hello koi world world")



""" 
Q - Given a sentence that consists of some words separated by a single space, and a searchWord, 
check if searchWord is a prefix of any word in sentence.
Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. 
If searchWord is a prefix of more than one word, return the index of the first word (minimum index). 
If there is no such word return -1 

A prefix of a string s is any leading contiguous substring of s.


Example 1:

Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
Example 2:

Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
Example 3:

Input: sentence = "i am tired", searchWord = "you"
Output: -1
Explanation: "you" is not a prefix of any word in the sentence.

"""

# ans - 1

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        splitted_sentence = sentence.split()
        found = False
        position = 1
        for index,word in enumerate(splitted_sentence):
            if word.find(searchWord) != -1:
                found = True
                position = index + 1
                break
        
        if found:
            return print(position)
        else:
            return print(-1)

# sol = Solution()
# print(sol.isPrefixOfWord("i love eating burger", "burg"))
# print(sol.isPrefixOfWord("this problem is an easy problem", "pro"))
# print(sol.isPrefixOfWord("i am tired", "you"))


# ans-2

class Solution:
    def isPrefixOfWord(self,sentence:str,searchWord:str) -> int:
        splitted_sentence = sentence.split()
        for index,word in enumerate(splitted_sentence):
            if word.startswith(searchWord):
                return index + 1
        return -1
    
# sol = Solution()
# print(sol.isPrefixOfWord("i love eating burger", "burg"))
# print(sol.isPrefixOfWord("this problem is an easy problem", "pro"))
# print(sol.isPrefixOfWord("i am tired", "you"))


"""
Q - Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

# ans-1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        elif s == ' ':
            return 1
        elif s != ' ' and len(s)==1:
            return 1
        else:
            length = 0
            word = ''
            large_word = ''
            large_length = 0
            for i in range(len(s)):
                for j in range(i,len(s)):
                    if s[j] in word:
                        if len(word) > len(large_word):
                            large_word = word
                            large_length = length
                        word = ''
                        length = 0
                        break
                    else:
                        word += s[j]
                        length += 1

            return large_length
    
# sol = Solution()
# sol.lengthOfLongestSubstring("abcabcbb")
# sol.lengthOfLongestSubstring("bbbbb")
# sol.lengthOfLongestSubstring("pwwkew")


"""
Q-Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

# ans-1
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:   
            median = (nums[len(nums)//2-1] + nums[len(nums)//2])/2
        else:
            median = nums[len(nums)//2]

        return median
    
sol = Solution()
sol.findMedianSortedArrays([1,3],[2,4])


"""
Q-Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

# ans

class Solution:
    def isValid(self,s:str) -> bool:
        bracket_map = {")":"(","]":"[","}":"{"}
        stack = []

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else "#"
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
    

sol = Solution()

# Example 1
print(sol.isValid("[)"))

# Example 2
print(sol.isValid("()[]{}"))

# Example 3
print(sol.isValid("([]){}")) 

# Example 4
print(sol.isValid("([])"))



