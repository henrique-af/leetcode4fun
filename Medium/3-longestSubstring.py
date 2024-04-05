class Solution(object):
    def lengthOfLongestSubstring(self, s):
        setter = set()
        l = 0
        result = 0
        for r in range (len(s)):
            while s[r] in setter:
                setter.remove(s[l])
                l += 1
            setter.add(s[r])
            result = max(result, r - l + 1)
        return result

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))

# LeetCode 3