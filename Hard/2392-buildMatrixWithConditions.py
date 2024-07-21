from collections import defaultdict, deque
from typing import List


class Solution:
    @staticmethod
    def topo_sort(k: int, conditions: List[List[int]]) -> List[int]:
        deg = [0] * (k + 1)
        adj = defaultdict(list)

        for v, w in conditions:
            adj[v].append(w)
            deg[w] += 1

        q = deque()
        for i in range(1, k + 1):
            if deg[i] == 0:
                q.append(i)

        count = 0
        ans = []
        while q:
            j = q.popleft()
            ans.append(j)
            count += 1
            for neighbor in adj[j]:
                deg[neighbor] -= 1
                if deg[neighbor] == 0:
                    q.append(neighbor)

        if count != k:
            return []  # has cycle
        else:
            return ans

    @staticmethod
    def dfs(k: int, conditions: List[List[int]]) -> deque:
        deg = [0] * (k + 1)
        adj = defaultdict(list)

        for v, w in conditions:
            adj[v].append(w)
            deg[w] += 1

        count = 0
        ans = deque()

        def f(i: int):
            nonlocal count
            deg[i] = -1  # mark as visited
            for j in adj[i]:
                if deg[j] == -1:
                    continue
                f(j)
            ans.appendleft(i)  # push front
            count += 1

        for i in range(1, k + 1):
            if deg[i] == 0:
                f(i)

        if count != k:
            return deque()  # might have cycle
        else:
            return ans

    @staticmethod
    def print_collection(c):
        print("[", end="")
        for i, x in enumerate(c):
            print(x, end=", " if i != len(c) - 1 else "")
        print("]")

    @staticmethod
    def buildMatrix(
        k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        order_row = Solution.topo_sort(k, rowConditions)
        order_col = Solution.topo_sort(k, colConditions)

        # print out the ordering in row & in col
        Solution.print_collection(order_row)
        Solution.print_collection(order_col)

        if not order_row or not order_col:
            return []  # some conflict

        arr = [[0] * k for _ in range(k)]
        # Find pos for x where 1<=x<=k
        pos_i = [-1] * (k + 1)
        pos_j = [-1] * (k + 1)

        for i in range(k):
            pos_i[order_row[i]] = i
            pos_j[order_col[i]] = i

        for x in range(1, k + 1):
            arr[pos_i[x]][pos_j[x]] = x

        return arr


k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]        
sol = Solution()
sol.buildMatrix(k, rowConditions, colConditions)
