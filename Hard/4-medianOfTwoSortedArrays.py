class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array = nums1 + nums2
        print(merged_array)
        merged_array.sort()
        print(merged_array)
        total_elements = len(merged_array)
        if total_elements % 2 == 1:
            median_index = total_elements // 2
            median = merged_array[median_index]
        else:
            median_index_1 = total_elements // 2 - 1
            median_index_2 = total_elements // 2
            median = (merged_array[median_index_1] + merged_array[median_index_2]) / 2.0
        return median


nums1 = [1, 2]
nums2 = [3, 4]

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))

# LeetCode 4
