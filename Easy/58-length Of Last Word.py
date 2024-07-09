class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(' ')
        last = words[-1]

        return len(last)
s = "   fly me   to   the moon  "
sol = Solution()
sol.lengthOfLastWord(s)
