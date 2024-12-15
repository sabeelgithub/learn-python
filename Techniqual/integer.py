"""
Q-Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""

# ans-1
class Solution:
    def logic(self,x:int) -> str:
        strx = str(x)
        rev_str = ''
        for i in strx:
            rev_str = i + rev_str
        return rev_str


    def reverse(self, x: int) -> int:
        if x < 0:
            x = x * -1
            rev_int = int(self.logic(x)) * -1
        else:
            rev_int = int(self.logic(x))

        if -2**31 <= rev_int <= 2**31-1:
            return rev_int
        else:
            return 0

sol = Solution()

# ans-2
class Solution():
    def reverse(self,x:int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev_x = int(str(x)[::-1]) * sign

        if -2**31 <= rev_x <= 2**31-1:
            return rev_x
        else:
            return 0


sol = Solution()

