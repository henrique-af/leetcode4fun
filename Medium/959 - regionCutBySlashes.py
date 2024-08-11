from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1, cols1 = len(grid), len(grid[0])
        rows2, cols2 = 3 * rows1, 3 * cols1
        grid2 = [[0] * cols2 for _ in range(rows2)]

        def fill(r, c, val):
            if 0 <= r < rows2 and 0 <= c < cols2:
                grid2[r][c] = val

        for r in range(rows1):
            for c in range(cols1):
                if grid[r][c] == "/":
                    # Barreira diagonal /
                    fill(r * 3, c * 3 + 2, 1)
                    fill(r * 3 + 1, c * 3 + 1, 1)
                    fill(r * 3 + 2, c * 3, 1)
                elif grid[r][c] == "\\":
                    # Barreira diagonal \
                    fill(r * 3, c * 3, 1)
                    fill(r * 3 + 1, c * 3 + 1, 1)
                    fill(r * 3 + 2, c * 3 + 2, 1)
                else:
                    # Sem barreira
                    fill(r * 3, c * 3, 0)
                    fill(r * 3 + 1, c * 3, 0)
                    fill(r * 3 + 2, c * 3, 0)
                    fill(r * 3, c * 3 + 1, 0)
                    fill(r * 3 + 1, c * 3 + 1, 0)
                    fill(r * 3 + 2, c * 3 + 1, 0)
                    fill(r * 3, c * 3 + 2, 0)
                    fill(r * 3 + 1, c * 3 + 2, 0)
                    fill(r * 3 + 2, c * 3 + 2, 0)

        # Função de busca para contagem de regiões
        def dfs(r, c):
            if r < 0 or r >= rows2 or c < 0 or c >= cols2 or grid2[r][c] == 1:
                return
            grid2[r][c] = 1
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        regions = 0
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c] == 0:
                    dfs(r, c)
                    regions += 1

        return regions


# Testando a solução
grid = ["/\\", "\\/"]
sol = Solution()
print(sol.regionsBySlashes(grid))  # Deve imprimir o número de regiões distintas
