class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        height = len(image)
        width = len(image[0])

        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            node = stack.pop()

            for dr, dc in directions:
                nr = node[0] + dr
                nc = node[1] + dc

                if (
                    nc < 0
                    or nc >= width
                    or nr < 0
                    or nr >= height
                    or image[nr][nc] != original_color
                ):
                    continue

                image[nr][nc] = color
                stack.append((nr, nc))
        return image
