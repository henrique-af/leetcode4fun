from typing import Counter, List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        count_arr = Counter(arr)
        distinct_elements = [char for char in arr if count_arr[char] == 1]

        if k <= len(distinct_elements):
            return distinct_elements[k - 1]
        return ""


arr = ["d","b","c","b","c","a"]
k = 2
sol = Solution()
print(sol.kthDistinct(arr, k))
