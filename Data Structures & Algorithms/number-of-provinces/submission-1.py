class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def mark_when_push(stack: list[int], visited: list[bool]) -> None:
            while stack:
                node = stack.pop()

                for i in range(len(isConnected[node])):
                    if isConnected[node][i] == 1 and not visited[i]:
                        stack.append(i)
                        visited[i] = True

        res = 0
        visited = [False] * len(isConnected[0])
        for i in range(len(visited)):
            if not visited[i]:
                visited[i] = True
                mark_when_push([i], visited)
                res += 1

        return res
