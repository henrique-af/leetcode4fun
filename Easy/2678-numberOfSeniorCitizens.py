from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for person in details:
            if int(person[11:13]) > 60:
                count += 1
        return count

details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
sol = Solution()
sol.countSeniors(details)
