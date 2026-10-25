class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        incoming = set()
        outgoing = set()

        for u, v in paths:
            outgoing.add(u)
            incoming.add(v)

        for place in incoming:
            if place not in outgoing:
                return place
        return ""
