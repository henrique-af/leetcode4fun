from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        index_map = {p: i for i, p in enumerate(positions)}
        positions.sort()

        stack = []
        for p in sorted(positions):
            i = index_map[p]

            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and directions[stack[-1]] == "R" and healths[i]:
                    j = stack.pop()

                    if healths[i] > healths[j]:
                        healths[j] = 0
                        healths[i] -= 1
                    elif healths[i] < healths[j]: 
                        healths[i] = 0
                        healths[j] -= 1
                        stack.append(j)
                    else:
                        healths[i] = healths[j] = 0
                if healths[i]:
                    stack.append(i)

        return [health for health in healths if health > 0]


positions = [5, 4, 3, 2, 1]
healths = [2, 17, 9, 15, 10]
directions = "RRRRR"
sol = Solution()
print(sol.survivedRobotsHealths(positions, healths, directions))
