class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs: list[int] = [0 for _ in range(len(s) + 1)]
        for ind in range(1, len(s) + 1):
            costs[ind] = costs[ind - 1] + abs(ord(s[ind - 1]) - ord(t[ind - 1]))

        res: int = 0

        for right_index in range(1, len(costs)):
            min_left: int = self.binary_search(costs, costs[right_index] - maxCost)
            if right_index - min_left > res:
                res = right_index - min_left

        return res

    def binary_search(self, arr, x) -> int:
        lo: int = 0
        hi: int = len(arr) - 1
        while lo < hi:
            mid: int = (lo + hi) // 2
            if arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

s = "abcd"
t = "bcdf"
maxCost = 3
sol = Solution()
sol.equalSubstring(s, t, maxCost)
