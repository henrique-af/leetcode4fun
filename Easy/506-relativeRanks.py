from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexed_scores = list(enumerate(score))

        sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)

        result = [""] * len(score)

        for rank, (index, _) in enumerate(sorted_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result


score = [5,4,3,2,1]
sol = Solution()
print(sol.findRelativeRanks(score))
