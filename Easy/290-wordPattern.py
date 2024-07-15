class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        reverse_mapping = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for p, word in zip(pattern, s):
            if p in mapping:
                if mapping[p] != word:
                    return False
            else:
                if word in reverse_mapping:
                    return False
                mapping[p] = word
                reverse_mapping[word] = p

        return True


pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
sol.wordPattern(pattern, s)
