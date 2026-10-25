class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degrees = [0] * (n + 2)
        out_degrees = [0] * (n + 2)

        for u, v in trust:
            in_degrees[u] += 1
            out_degrees[v] += 1
        
        for i in range(1, len(in_degrees)):
            if in_degrees[i] == 0 and out_degrees[i] == n - 1:
                return i
        return -1