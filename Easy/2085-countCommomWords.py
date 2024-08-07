from typing import Counter, List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)

        return sum(1 for word in count1 if count1[word] == 1 and count2[word] == 1)
        
words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
sol = Solution()
print(sol.countWords(words1, words2))