class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I": 1,
            "V": 5,
            'X': 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result  = 0

        for i in range(len(s) -1):
            current = symbol[s[i]]
            next = symbol[s[i + 1]]
            if current >= next:
                result += current
            else:
                result -= current
        
        
        result += symbol[s[-1]]
        return result