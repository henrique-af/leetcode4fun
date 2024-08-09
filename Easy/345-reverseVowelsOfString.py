class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        first, second = 0, len(s) - 1
        while first < second:
            if s[first] in vowels and s[second] in vowels:
                s[first], s[second] = s[second], s[first]
                first += 1
                second -= 1
            if s[first] not in vowels:
                first += 1
            if s[second] not in vowels:
                second -= 1
        return ''.join(s)
    
s = "hello"                
sol = Solution()
sol.reverseVowels(s)