from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(x):
            x_len = len(x)
            if x_len <= 0:
                return False
            x_list = list(map(str, x))
            count = len(x_list) - 1
            x_reversed = []
            for i in range(len(x_list)):
                x_reversed.append(x_list[count])
                count -= 1
            return x_list == x_reversed

        for word in words:
            if isPalindrome(word):
                return word
        return ""

words = ["abc", "car", "ada", "racecar", "cool"]
sol = Solution()
sol.firstPalindrome(words)