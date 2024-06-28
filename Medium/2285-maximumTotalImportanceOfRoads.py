from collections import defaultdict
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connections = defaultdict(int)
        for a, b in roads:
            connections[a] += 1
            connections[b] += 1

        sorted_cities = sorted(connections.keys(), key=lambda x: -connections[x])
        values = [0] * n
        for i, city in enumerate(sorted_cities):
            values[city] = n - i
        total_importance = 0
        for a, b in roads:
            total_importance += values[a] + values[b]

        return total_importance


n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
sol = Solution()
print(sol.maximumImportance(n, roads))
