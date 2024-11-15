from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1

            for j in range(i, n):
                if s[i:j+1] in word_set:
                    dp[i] = min(dp[i], dp[j + 1])
        
        return dp[0]

s = "dwmodizxvvbosxxw"
dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]  
sol = Solution()
sol.minExtraChar(s, dictionary)