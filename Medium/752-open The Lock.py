from typing import List

from collections import deque

class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        
        start = "0000"
        if start in deadends:
            return -1
        if target in deadends:
            return -1
        
        queue = deque([(start, 0)])
        
        visited = set(start)
        
        def neighbors(state):
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    yield state[:i] + str(new_digit) + state[i+1:]
        
        while queue:
            state, moves = queue.popleft()
            
            if state == target:
                return moves

            for neighbor in neighbors(state):
                if neighbor not in deadends and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, moves + 1))
                    
        return -1


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
sol = Solution()
sol.openLock(deadends, target)