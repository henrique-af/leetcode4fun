from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = [0] * len(nums)
        prefix_sums[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i]

        def binary_search(prefix_sums, query):
            left, right = 0, len(prefix_sums)
            while left < right:
                mid = (left + right) // 2
                if prefix_sums[mid] <= query:
                    left = mid + 1
                else:
                    right = mid
            return left

        answer = []
        for query in queries:
            idx = binary_search(prefix_sums, query)
            answer.append(idx)

        return answer


nums = [4, 5, 2, 1]
queries = [3, 10, 21]
sol = Solution()
print(sol.answerQueries(nums, queries))
