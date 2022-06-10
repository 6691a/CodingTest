class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = []
        for x in zip(*strs):
            print(x)
            if len(set(x)) ==1:
                answer.append(x[0])
            else:
                break
        print(''.join(answer))
        return ''.join(answer) 

strs = ["flower", "flow", "flight"]
Solution().longestCommonPrefix(strs)