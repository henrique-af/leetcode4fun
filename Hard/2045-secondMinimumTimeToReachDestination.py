import heapq
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dis1 = [float('inf')] * (n + 1)
        dis2 = [float('inf')] * (n + 1)

        pq = [(0, 1)]

        while pq:
            timepassed, node = heapq.heappop(pq)

            if node == n and dis2[n] != float('inf'):
                return dis2[n]

            div = timepassed // change
            if div % 2 == 1:
                timepassed = change * (div + 1)

            for nbr in adj[node]:
                if dis1[nbr] > timepassed + time:
                    dis2[nbr] = dis1[nbr]
                    dis1[nbr] = timepassed + time
                    heapq.heappush(pq, (timepassed + time, nbr))
                elif dis2[nbr] > timepassed + time and dis1[nbr] != timepassed + time:
                    dis2[nbr] = timepassed + time
                    heapq.heappush(pq, (timepassed + time, nbr))

        return -1

sol = Solution()
n = 5
edges = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 5], [4, 5]]
time = 3
change = 5
print(sol.secondMinimum(n, edges, time, change))