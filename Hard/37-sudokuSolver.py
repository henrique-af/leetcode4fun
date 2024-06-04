from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i].add(num)
                    columns[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        def backtrack(i, j):
            if i == 9:
                return True

            if board[i][j] != ".":
                return backtrack(i + (j + 1) // 9, (j + 1) % 9)

            for num in range(1, 10):
                box_index = (i // 3) * 3 + (j // 3)
                if (
                    num not in rows[i]
                    and num not in columns[j]
                    and num not in boxes[box_index]
                ):
                    rows[i].add(num)
                    columns[j].add(num)
                    boxes[box_index].add(num)
                    board[i][j] = str(num)

                    if backtrack(i + (j + 1) // 9, (j + 1) % 9):
                        return True

                    rows[i].remove(num)
                    columns[j].remove(num)
                    boxes[box_index].remove(num)
                    board[i][j] = "."

            return False

        backtrack(0, 0)


# Example usage
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sol = Solution()
sol.solveSudoku(board)
for row in board:
    print(row)
