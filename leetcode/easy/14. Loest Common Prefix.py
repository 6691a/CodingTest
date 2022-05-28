class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = []
        for x in zip(*strs):
            if len(set(x)) ==1:
                answer.append(x[0])
            else:
                break
        return ''.join(answer) 

Solution().longestCommonPrefix(["flower", "flow", "flight"])