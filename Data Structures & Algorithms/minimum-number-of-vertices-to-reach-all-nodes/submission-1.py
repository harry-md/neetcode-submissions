class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()

        for u, v in edges:
            incoming.add(v)
        
        return [i for i in range(n) if i not in incoming]
