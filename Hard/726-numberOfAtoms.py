from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == "(":
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ")":
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][atom] += count

        result = []
        for atom in sorted(stack[-1]):
            count = stack[-1][atom]
            result.append(f"{atom}{count if count > 1 else ''}")

        return "".join(result)


formula = "K4(ON(SO3)2)2"
sol = Solution()
print(sol.countOfAtoms(formula))
