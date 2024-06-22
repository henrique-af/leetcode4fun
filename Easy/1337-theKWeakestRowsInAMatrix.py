from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        order = {i: sum(row) for i, row in enumerate(mat)}
        sorted_indices = sorted(order, key=order.get)
        return sorted_indices[:k]


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]
k = 3
sol = Solution()
result = sol.kWeakestRows(mat, k)
print(result)
