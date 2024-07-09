from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]
        end = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{end}")
                start = nums[i]
                end = nums[i]

        if start == end:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{end}")

        return ranges


nums = [0, 1, 2, 4, 5, 7]
sol = Solution()
sol.summaryRanges(nums)
