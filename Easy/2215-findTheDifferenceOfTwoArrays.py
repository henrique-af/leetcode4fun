from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in answer[0]:
                answer[0].append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in answer[1]:
                answer[1].append(nums2[i])  
        print(answer)
        return answer


class Solution2:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        answer = [list(set1 - set2), list(set2 - set1)]
        print(answer)
        return answer


nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
sol = Solution2()
sol.findDifference(nums1, nums2)
