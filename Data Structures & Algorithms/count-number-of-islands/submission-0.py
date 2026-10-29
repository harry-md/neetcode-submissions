class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(stack: list[tuple[int, int]]):
            while stack:
                node = stack.pop()

                for dr, dc in directions:
                    nr = node[0] + dr
                    nc = node[1] + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != "1":
                        continue

                    grid[nr][nc] = "0"

                    stack.append((nr, nc))

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    dfs([(r, c)])
                    res += 1
        return res
