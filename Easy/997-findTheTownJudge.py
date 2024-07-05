from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trusts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        
        for a, b in trust:
            trusts[a] += 1
            trusted_by[b] += 1
        
        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted_by[i] == n - 1:
                return i

        return -1

sol = Solution()
n = 3
trust = [[1, 3], [2, 3]]
print(sol.findJudge(n, trust)) 