from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        if k == 0:
            return [0] * n
        
        def circular_sum(index):
            if k > 0:
                return sum(code[(index + i) % n] for i in range(1, k + 1))
            else:
                return sum(code[(index - i) % n] for i in range(1, -k + 1))
        
        return [circular_sum(i) for i in range(n)]
                
        
        
code = [5, 7, 1, 4]
k = 3
sol = Solution()
print(sol.decrypt(code, k))