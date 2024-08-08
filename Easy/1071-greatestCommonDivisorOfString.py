class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def canForm(s, x):
            return x * (len(s) // len(x)) == s

        len1, len2 = len(str1), len(str2)

        gcd_len = gcd(len1, len2)

        candidate = str1[:gcd_len]

        if canForm(str1, candidate) and canForm(str2, candidate):
            return candidate
        else:
            return ""


str1 = "ABCABC"
str2 = "ABC"        
sol = Solution()
print(sol.gcdOfStrings(str1, str2))
