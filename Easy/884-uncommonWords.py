from typing import Counter, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split()) + Counter(s2.split())
        
        return [word for word in count if count[word] == 1]
        
        
        
sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(sol.uncommonFromSentences(s1, s2))