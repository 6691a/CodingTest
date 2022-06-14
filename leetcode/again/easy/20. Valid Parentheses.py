class Solution:
    def isValid(self, s: str) -> bool:
        symbol = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        res = []
        for i in s:
            if i in symbol:
                res.append(i)
            else:
                if not res or symbol[res.pop()] != i:
                    return False
        return not res

print(Solution().isValid("["))