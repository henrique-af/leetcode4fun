from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            width = 0
            height = 0
            dp[i] = float('inf')
            
            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)
        
        return dp[n]

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
sol = Solution()
sol.minHeightShelves(books, shelfWidth)