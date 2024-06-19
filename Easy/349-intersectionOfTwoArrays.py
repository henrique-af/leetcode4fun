from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        a = []
        i = 0

        for i in range(n):
            if nums1[i] in nums2:
                a.append(nums1[i])
        a = list(dict.fromkeys(a))
        return a


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
print(sol.intersection(nums1, nums2))
