from typing import List

def movement(vector, row, col):
    if vector == 0: 
        row -= 1
    elif vector == 1:
        col += 1
    elif vector == 2:
        row += 1
    elif vector == 3:
        col -= 1
    return row, col

def change_vector(vector):
    return (vector + 1) % 4

def border_is_good(cRow, cCol, rows, cols):
    return 0 <= cRow < rows and 0 <= cCol < cols

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        matrix = [[0] * 2 for _ in range(rows * cols)]
        matrix[0] = [rStart, cStart]

        total = rows * cols
        visited = 1
        travel_length = 1
        vector = 1 
        k = 1
        freq = 0

        while visited < total:
            freq += 1
            for _ in range(travel_length):
                rStart, cStart = movement(vector, rStart, cStart)
                if border_is_good(rStart, cStart, rows, cols):
                    matrix[k] = [rStart, cStart]
                    k += 1
                    visited += 1
                    if visited == total:
                        return matrix

            vector = change_vector(vector)
            if freq == 2:
                freq = 0
                travel_length += 1

        return matrix

rows = 1
cols = 4
rStart = 0
cStart = 0
sol = Solution()
print(sol.spiralMatrixIII(rows, cols, rStart, cStart))