class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i, j = 0, 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res += word1[i]
                i += 1
            if j < len(word2):
                res += word2[j]
                j += 1
        return res

word1 = "abc"
word2 = "pqqqqqq"
sol = Solution()
print(sol.mergeAlternately(word1, word2))
