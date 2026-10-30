class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(queue: deque[tuple[int, int]], visited: set[tuple[int, int]]) -> int:
            res = 0
            while queue:
                size = len(queue)

                for _ in range(size):
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (
                            nr < 0
                            or nr >= ROWS
                            or nc < 0
                            or nc >= COLS
                            or grid[nr][nc] != 1
                            or (nr, nc) in visited
                        ):
                            continue

                        grid[nr][nc] = 2
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                res += 1
            return max(res - 1, 0)

        visited = set()
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        res = bfs(queue, visited)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return res