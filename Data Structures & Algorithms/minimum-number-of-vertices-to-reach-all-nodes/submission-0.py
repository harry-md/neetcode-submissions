class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming, outgoing = set(), set()

        for u, v in edges:
            outgoing.add(u)
            incoming.add(v)
        
        res = []

        for i in range(n):
            if i in incoming:
                continue
            res.append(i)
        return res
