from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda x: (x[1], -x[0]))
        
        result = []
        for num, freq in sorted_items:
            result.extend([num] * freq)
        
        return result

# Teste
nums = [1, 1, 2, 2, 2, 3]
sol = Solution()
print(sol.frequencySort(nums))
