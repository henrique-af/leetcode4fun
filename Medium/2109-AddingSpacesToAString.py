from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        last_index = 0
        for space in spaces:
            result.append(s[last_index:space])
            result.append(" ")
            last_index = space
        result.append(s[last_index:])
        return "".join(result)

        

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]        
sol = Solution()
sol.addSpaces(s, spaces)