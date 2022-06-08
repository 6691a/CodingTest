class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        value = 0
        for i in range(len(s) -1):
            current = s[i]
            next = s[i + 1]
            if symbol[current] < symbol[next]:
                value -= symbol[current]
            else:
                value += symbol[current]
        value += symbol[s[len(s) -1]]
        return value