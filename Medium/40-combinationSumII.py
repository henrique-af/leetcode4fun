from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()
        res = []
        backtrack(0, target, [])
        return res


candidates = [10,1,2,7,6,1,5]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))
