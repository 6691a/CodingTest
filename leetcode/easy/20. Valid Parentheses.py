class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(':')',
            '{':'}',
            '[':']'
        }
        list = []
        for c in s:
            if c in dict:
                list.append(c)
            elif len(list) == 0 or dict[list.pop()] != c:
                return False
        return not list