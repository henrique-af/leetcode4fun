from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def backtracking(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for letter in keyboard[next_digits[0]]:
                    backtracking(combination + letter, next_digits[1:])

        if digits:
            backtracking("", digits)
        return res

digits = "23"
sol = Solution()
print(sol.letterCombinations(digits))
