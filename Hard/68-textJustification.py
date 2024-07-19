from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        num_of_letters = 0

        for word in words:
            if num_of_letters + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    line[i % (len(line) - 1 or 1)] += " "
                res.append("".join(line))
                line = []
                num_of_letters = 0

            line.append(word)
            num_of_letters += len(word)

        res.append(" ".join(line).ljust(maxWidth))
        return res


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
sol = Solution()
sol.fullJustify(words, maxWidth)
