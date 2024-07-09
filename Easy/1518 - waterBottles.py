class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new = empty // numExchange
            total += new
            empty = new + (empty % numExchange)

        return total


sol = Solution()
numBottles = 9
numExchange = 3
print(sol.numWaterBottles(numBottles, numExchange))
