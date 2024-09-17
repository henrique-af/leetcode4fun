from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude, current_altitude = 0, 0
        for value in gain:
            current_altitude += value
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude

sol = Solution()
gain = [-5,1,5,0,-7]
sol.largestAltitude(gain)