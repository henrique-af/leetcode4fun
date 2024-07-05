from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)

        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1


sol = Solution()
nums1 = [1,2,3]
nums2 = [2,4]
print(sol.getCommon(nums1, nums2))
