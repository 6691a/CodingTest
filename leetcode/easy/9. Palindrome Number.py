# https://leetcode.com/problems/palindrome-number/

# string ver
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) != str(x)[::-1]:
            return False
        return True
