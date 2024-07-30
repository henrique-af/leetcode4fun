class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a = s.count('a')
        total_b = s.count('b')
        
        count_a_after = total_a
        count_b_before = 0
        min_deletions = float('inf')
        
        for char in s:
            if char == 'a':
                count_a_after -= 1
            else:  # char == 'b'
                count_b_before += 1
            
            deletions = count_b_before + count_a_after
            min_deletions = min(min_deletions, deletions)
        
        min_deletions = min(min_deletions, total_b)
        min_deletions = min(min_deletions, total_a)

        return min_deletions
        
s = "aababbab"
sol = Solution()
print(sol.minimumDeletions(s))