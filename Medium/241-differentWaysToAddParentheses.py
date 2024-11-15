from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str):
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]
            
            results = []
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    for left in left_results:
                        for right in right_results:
                            if expr[i] == '+':
                                results.append(left + right)
                            elif expr[i] == '-':
                                results.append(left - right)
                            elif expr[i] == '*':
                                results.append(left * right)
            
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return compute(expression)
    
sol = Solution()
expression = "2-1-1"
print(sol.diffWaysToCompute(expression))