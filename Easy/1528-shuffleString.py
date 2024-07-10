from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        stringDict = {}
        for idx, char in enumerate(s):
            stringDict[indices[idx]] = char
        
        returnString = ""

        for i in range(len(s)):
            print(i)
            returnString += stringDict[i]
        return returnString

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sol = Solution()
print(sol.restoreString(s, indices))
