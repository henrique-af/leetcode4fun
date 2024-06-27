from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        node_count = {}

        for edge in edges:
            for node in edge:
                if node in node_count:
                    node_count[node] += 1
                else:
                    node_count[node] = 1

        for node, count in node_count.items():
            if count == n:
                return node

        return -1


edges = [[1, 3], [2, 3]]
sol = Solution()
print(sol.findCenter(edges))
