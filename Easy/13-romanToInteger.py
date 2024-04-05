class Solution(object):
    def romanToInt(self, s):
        mapper = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev_value = 0
        for char in s:
            value = mapper[char]
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
        return total


sol = Solution()
print(sol.romanToInt("III"))
