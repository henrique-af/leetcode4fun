class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_filtered = ""
    
        for char in s:
            if char.isalnum():
                s_filtered += char
        
        return True if s_filtered == s_filtered[::-1] else False

s = "A man, a plan, a canal: Panama"
sol = Solution()
sol.isPalindrome(s)