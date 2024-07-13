class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s: str, pair: str, score: int) -> (int, str):
            res = 0
            stack = []

            for char in s:
                if char == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(char)
            return res, "".join(stack)

        res = 0

        pair = "ab" if x > y else "ba"
        max_score = max(x, y)
        min_score = min(x, y)
        points, s = remove_pairs(s, pair, max_score)
        res += points
        points, s = remove_pairs(s, pair[::-1], min_score)
        res += points

        return res


s = "cdbcbbaaabab"
x = 4
y = 5
sol = Solution()
sol.maximumGain(s, x, y)
