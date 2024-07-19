class Solution:
    def reverseWords(self, s: str) -> str:
        s_splitted = s.split()
        res = []
        n = len(s_splitted)
        for i in range(n - 1, -1, -1):
            res.append(s_splitted[i])
        return " ".join(res)

s = "the sky is blue"
sol = Solution()
print(sol.reverseWords(s))
