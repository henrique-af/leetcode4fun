from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = zip(names, heights)
        zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        res = []
        for name, height in zipped:
            res.append(name)

        return res
            

names = ["Mary","John","Emma"]
heights = [180,165,170]
sol = Solution()
sol.sortPeople(names, heights)
