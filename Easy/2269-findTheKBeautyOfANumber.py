class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        n = len(num_str)
        count = 0

        for i in range(n - k + 1):
            substring = num_str[i : i + k]
            if substring == "0":
                continue
            substring_num = int(substring)
            if substring_num != 0 and num % substring_num == 0:
                count += 1

        return count


num = 240
k = 2
sol = Solution()
sol.divisorSubstrings(num, k)
