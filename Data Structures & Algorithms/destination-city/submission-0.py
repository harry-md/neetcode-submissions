class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from collections import defaultdict
        in_degrees = defaultdict(bool)
        out_degrees = defaultdict(bool)

        for u, v in paths:
            out_degrees[u] = True
            in_degrees[v] = True

        for place in in_degrees:
            if place not in out_degrees:
                return place
        return ""
