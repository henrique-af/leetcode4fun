from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        num_rows = len(matrix)

        lucky_numbers = []


        for row in range(num_rows):
            row_min = min(matrix[row])
            col_index = matrix[row].index(row_min)

            is_lucky = True
            for r in range(num_rows):
                if matrix[r][col_index] > row_min:
                    is_lucky = False
                    break

            if is_lucky:
                lucky_numbers.append(row_min)

        return lucky_numbers



matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
sol = Solution()
print(sol.luckyNumbers(matrix)) 
