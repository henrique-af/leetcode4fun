class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        res = ""

        for n in binary:
            if n == "0":
                res += "1"
            else:
                res += "0"

        return int(res, 2)

sol = Solution()
print(sol.findComplement(5))
