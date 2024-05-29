class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        steps = 0
        while s != 1:
            if s % 2 == 0:  
                s //= 2
            else: 
                s += 1
            steps += 1
        return steps


s = "1101"
sol = Solution()
print(sol.numSteps(s))