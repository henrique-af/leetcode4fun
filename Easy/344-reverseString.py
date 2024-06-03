from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i in range(length):
            s.insert(i, s.pop())
        print(s)


s = ["h", "e", "l", "l", "o"]
sol = Solution()
sol.reverseString(s)
