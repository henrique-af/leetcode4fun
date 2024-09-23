class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        lps = self.computeKMP(combined)
        longest_palindromic_prefix_length = lps[-1]
        
        return rev_s[:len(s) - longest_palindromic_prefix_length] + s

    def computeKMP(self, pattern: str) -> list:
        n = len(pattern)
        lps = [0] * n
        length = 0 
        
        i = 1
        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
