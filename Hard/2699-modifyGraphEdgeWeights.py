import heapq
from typing import List, Tuple

class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.adj = []
        self.wild_edges = []

    def build_graph(self, edges: List[List[int]]):
        for i in range(self.m):
            u, v, w = edges[i]
            if w > 0:
                self.adj[u].append((w, v))
                self.adj[v].append((w, u))
            else:
                self.wild_edges.append(i)

    def dijkstra(self, src: int, des: int, adj: List[List[Tuple[int, int]]]) -> int:
        dist = [float('inf')] * self.n
        pq = []
        heapq.heappush(pq, (0, src))
        dist[src] = 0

        while pq:
            d0, i = heapq.heappop(pq)
            if i == des:
                return d0
            for d_next, j in adj[i]:
                new_d = d0 + d_next
                if new_d < dist[j]:
                    dist[j] = new_d
                    heapq.heappush(pq, (new_d, j))
        return float('inf')

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.m = len(edges)
        self.build_graph(edges)

        dist = self.dijkstra(source, destination, self.adj)
        if dist < target:
            return []

        for i in self.wild_edges:
            edges[i][2] = target + 1  # weight = target + 1
        if dist == target:
            return edges

        for i in self.wild_edges:
            new_edge = edges[i]
            u, v = new_edge[0], new_edge[1]
            new_edge[2] = 1
            self.adj[u].append((1, v))
            self.adj[v].append((1, u))
            dist = self.dijkstra(source, destination, self.adj)
            if dist <= target:
                new_edge[2] += target - dist
                return edges

        return []