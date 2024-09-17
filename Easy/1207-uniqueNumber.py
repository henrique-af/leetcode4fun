from typing import Counter, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        
        occurrence = list(freq.values())
        
        return len(occurrence) == len(set(occurrence))
        
sol = Solution()
arr = [1,2,2,1,1,3]
sol.uniqueOccurrences(arr)