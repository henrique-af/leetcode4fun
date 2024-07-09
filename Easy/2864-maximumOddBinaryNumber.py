class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = ""
        ones = ""
        for number in s:
            if number == "1":
                ones += number
            if number == "0" :
                zeros += number
        return str(ones[:len(ones) - 1] + zeros + "1")


s = "0101"
sol = Solution()
print(sol.maximumOddBinaryNumber(s))
