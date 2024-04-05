class Solution:
    def reverse(self, x: int) -> int:
        min = -2 ** 31
        max = 2 ** 31 - 1

        negative = x < 0
        if negative:
            x = -x

        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x//=10
        if negative:
            reversed_x = -reversed_x
        if reversed_x < min or reversed_x > max:
            return 0

        return reversed_x


sol = Solution()
print(sol.reverse(123))