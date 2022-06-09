class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        len(s.split(" ")[-1])