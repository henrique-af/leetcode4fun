from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1  # Minimum possible distance
        r = position[-1] - position[0]  # Maximum possible distance

        def good(target):
            balls = 1
            last_basket = position[0]

            for i in range(1, len(position)):
                if position[i] - last_basket >= target:
                    balls += 1
                    last_basket = position[i]
                    if balls == m:
                        return True
            return False

        while l <= r:
            mid = (l + r) // 2

            if good(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r


# Example usage
sol = Solution()
position = [1, 2, 3, 4, 7]
m = 3
print(sol.maxDistance(position, m))  # Output: 3


position = [1, 2, 3, 4, 7]
m = 3
sol = Solution()
sol.maxDistance(position, m)
