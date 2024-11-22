from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)
        for row in matrix:
            pattern = tuple(row)
            flipped = tuple(1 - x for x in row) 
            
            pattern_count[pattern] += 1
            pattern_count[flipped] += 1
            
        return max(pattern_count.values())
            
            
            
            
        
matrix = [[0, 1], [1, 1]]        
sol = Solution()
sol.maxEqualRowsAfterFlips(matrix)