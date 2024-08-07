class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            switcher = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
            }
            return switcher.get(num, "")

        def two_less_20(num):
            switcher = {
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen",
            }
            return switcher.get(num, "")

        def ten(num):
            switcher = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety",
            }
            return switcher.get(num, "")

        def two(num):
            if not num:
                return ""
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                remainder = num - tenner * 10
                return ten(tenner) + ("" if remainder == 0 else " " + one(remainder))

        def three(num):
            hundred = num // 100
            remainder = num - hundred * 100
            if hundred and remainder:
                return one(hundred) + " Hundred " + two(remainder)
            elif not hundred and remainder:
                return two(remainder)
            elif hundred and not remainder:
                return one(hundred) + " Hundred"
            else:
                return ""

        units = ["", " Thousand", " Million", " Billion"]
        result = []
        unit_index = 0

        while num > 0:
            if num % 1000 != 0:
                result.append(three(num % 1000) + units[unit_index])
            num //= 1000
            unit_index += 1

        return " ".join(result[::-1]).strip()


# Exemplo de uso
sol = Solution()
print(sol.numberToWords(123))
print(sol.numberToWords(1234567))
print(sol.numberToWords(1000000000))=
