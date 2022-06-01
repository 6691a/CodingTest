class Solution:
    def isPalindrome(self, x: int) -> bool:
        answer = 0
        input = x

        while input > 0:
            answer = answer * 10 + input % 10
            input = input // 10
        
        return answer == x
