import re
from typing import List


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        def find_numbers(s: str) -> List[int]:
            numbers = re.findall(r"\d+", s)
            numbers = [int(num) for num in numbers]
            return numbers

        num_list = find_numbers(s)
        n = len(num_list)

        for i in range(n - 1):
            if num_list[i] >= num_list[i + 1]:
                return False
        return True


s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
sol = Solution()
print(sol.areNumbersAscending(s))
