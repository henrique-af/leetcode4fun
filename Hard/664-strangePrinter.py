class Solution:
    def __init__(self):
        self.n = 1
        self.alphabet = [[] for _ in range(26)]

    def shorten(self, s):
        s = list(s)  # Convert string to a list to allow in-place modification
        sz = len(s)
        l = 0
        r = 1
        
        while r < sz:
            cur = s[r]
            while l < r and s[l] == cur:
                l += 1
            if r < sz and s[l] != cur:
                self.alphabet[ord(cur) - ord('a')].append(self.n)
                s[self.n] = cur
                self.n += 1
                l = r
            r += 1
        
        s = ''.join(s[:self.n])  # Shorten the string to its new size
        return s

    def strangePrinter(self, s):
        s = self.shorten(s)
        n = self.n
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1  # Base case: a single character needs 1 operation
            for j in range(i + 1, n):
                x = dp[i][j - 1]
                if s[i] == s[j]:
                    dp[i][j] = x
                    continue
                x += 1
                if j - i <= 5:
                    for k in range(i + 1, j):
                        if s[k] == s[j]:
                            x = min(x, dp[i][k - 1] + dp[k][j - 1])
                            k += 1
                else:
                    K = self.alphabet[ord(s[j]) - ord('a')]
                    l = next((k for k in range(len(K)) if K[k] > i), len(K))
                    for k in range(l, len(K)):
                        if K[k] < j:
                            x = min(x, dp[i][K[k] - 1] + dp[K[k]][j - 1])
                        else:
                            break
                dp[i][j] = x
        
        return dp[0][n - 1]
