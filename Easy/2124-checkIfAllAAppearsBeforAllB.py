class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s


s = "aaabbb"
sol = Solution()
print(sol.checkString(s))
