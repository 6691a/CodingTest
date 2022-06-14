class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, res = 0, ""

        a = list(a)
        b = list(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            
            if b:
                carry += int(b.pop())
            

            res += str(carry % 2)
            carry //= 2
        
        return res[::-1]

Solution().addBinary("11", "1")