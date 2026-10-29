class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(queue: deque[tuple[int, int]]) -> None:
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0":
                        continue

                    grid[nr][nc] = "0"
                    queue.append((nr, nc))

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = "0"

                    queue = deque()
                    queue.append((r, c))
                    bfs(queue)
                    res += 1
        return res
