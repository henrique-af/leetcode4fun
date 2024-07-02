class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s[i] not in s[i + 1 :] and s[i] not in s[:i]:
                return i
        return -1


s = "leetcode"
sol = Solution()
print(sol.firstUniqChar(s))
