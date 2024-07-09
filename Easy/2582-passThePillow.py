class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = (n - 1) * 2
        remainder_time = time % cycle_length

        if remainder_time < n:
            return remainder_time + 1
        else:
            return cycle_length - remainder_time + 1


n = 3
time = 2
sol = Solution()
print(sol.passThePillow(n, time))
