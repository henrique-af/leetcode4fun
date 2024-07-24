from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i, n in enumerate(nums):
            n = str(n)
            mappedNums = 0
            for c in n:
                mappedNums *= 10
                mappedNums += mapping[int(c)]

            pairs.append((mappedNums, i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]



mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
sol = Solution()
sol.sortJumbled(mapping, nums)