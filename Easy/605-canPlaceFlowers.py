from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        length = len(flowerbed)

        while i < length:
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == length - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                count += 1
            i += 1

        return count >= n


flowerbed = [1,0,0,0,1]
n = 1
sol = Solution()
print(sol.canPlaceFlowers(flowerbed, n))
