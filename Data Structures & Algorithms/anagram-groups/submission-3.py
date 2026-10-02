class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def to_key(s: str) -> List[int]:
            arr = [0] * 26
            for i in s:
                arr[ord(i) - ord('a')] += 1
            return "#".join([str(a) for a in arr])
        
        res = defaultdict(list)
        for s in strs:
            res[to_key(s)].append(s)
        return list(res.values())