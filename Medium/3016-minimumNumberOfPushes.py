class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [0] * 26
        for char in word:
            counts[ord(char) - ord("a")] += 1
        counts.sort(reverse=True)

        res = 0
        distinct = 0
        for count in counts:
            if count > 0:
                res += count * (1 + distinct // 8)
                distinct += 1
        return res

word = "abcde"
sol = Solution()
print(sol.minimumPushes(word))