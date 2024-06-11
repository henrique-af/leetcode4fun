from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        result = []

        for num in arr2:
            result.extend([num] * count[num])
            del count[num]  

        for num in sorted(count.elements()):
            result.append(num)

        return result


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
sol = Solution()
print(sol.relativeSortArray(arr1, arr2))  # Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
