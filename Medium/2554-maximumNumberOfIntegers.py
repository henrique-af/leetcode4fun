class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        x_not = set(banned)  # Use a set to store banned numbers
        total_sum = 0
        count = 0
        
        for x in range(1, n + 1):
            if x not in x_not:
                total_sum += x
                if total_sum > maxSum:  # Stop if the sum exceeds maxSum
                    break
                count += 1
                
        return count
