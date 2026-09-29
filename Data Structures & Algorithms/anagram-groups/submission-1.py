class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toTuple(s: str):
            arr = [0] * 26
            for i in s:
                arr[ord(i) - ord('a')] += 1
            return tuple(arr)
        
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[toTuple(s)].append(s)
        return list(hashmap.values())

        