def expandFromMiddle(s: str, left: int, right: int) -> int:
    if s == "" or left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s) < 1:
            return ""
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = expandFromMiddle(s, i, i)
            len2 = expandFromMiddle(s, i, i + 1)
            lenMax = max(len1, len2)

            if lenMax > end - start:
                start = i - ((lenMax - 1) // 2)
                end = i + (lenMax // 2)

        return s[int(start) : int(end) + 1]


sol = Solution()
print(sol.longestPalindrome("cbbd"))

# LeetCode 5