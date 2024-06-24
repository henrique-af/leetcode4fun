from typing import List
import collections


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        count = 0
        flipped = 0
        outs = collections.deque()

        for i in range(n):
            if len(outs) > 0 and outs[0] == i:
                outs.popleft()
                flipped = not flipped

            if nums[i] == flipped:
                flipped ^= 1
                count += 1
                outs.append(i + k)

        if len(outs) > 0 and outs[0] == n:
            outs.popleft()

        if len(outs) > 0:
            return -1
        return count


nums = [0, 1, 0]
k = 1

sol = Solution()
print(sol.minKBitFlips(nums, k))
