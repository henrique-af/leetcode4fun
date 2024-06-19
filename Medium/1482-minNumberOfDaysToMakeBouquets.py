from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
            def canMakeBouquets(mid: int) -> bool:
                bouquets = 0
                flowers = 0
                for bloom in bloomDay:
                    if bloom <= mid:
                        flowers += 1
                        if flowers == k:
                            bouquets += 1
                            flowers = 0
                    else:
                        flowers = 0
                    if bouquets >= m:
                        return True
                return False

            n = len(bloomDay)
            if n < m * k:
                return -1

            low, high = min(bloomDay), max(bloomDay)
            while low < high:
                mid = (low + high) // 2
                if canMakeBouquets(mid):
                    high = mid
                else:
                    low = mid + 1

            return low

bloomDay = [1,10,3,10,2]
m = 3 ## buques
k = 1 ## adjacente
sol = Solution()
sol.minDays(bloomDay, m, k)