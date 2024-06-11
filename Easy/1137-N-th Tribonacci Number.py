class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        t0 = 0
        t1, t2 = 1, 1

        for i in range(3, n + 1):
            tn = t0 + t1 + t2
            t0, t1, t2 = t1, t2, tn

        return t2


sol = Solution()
print(sol.tribonacci(4))