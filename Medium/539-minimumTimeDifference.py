from typing import List
from datetime import datetime

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_converted = [datetime.strptime(time, "%H:%M") for time in timePoints]
        time_converted.sort()
        
        minutes = [t.hour * 60 + t.minute for t in time_converted]
        
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
       
        min_diff = min(min_diff, (1440 - minutes[-1] + minutes[0]))
        
        return min_diff
    
        

timePoints = ["23:59","00:00"]      
sol = Solution()
print(sol.findMinDifference(timePoints))