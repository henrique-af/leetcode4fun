from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minValue = float("inf")
        maxProfit = 0 

        for price in prices:
            if price < minValue:
                minValue = price 
            elif price - minValue > maxProfit:
                maxProfit = (
                    price - minValue
                )

        return maxProfit


prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))
