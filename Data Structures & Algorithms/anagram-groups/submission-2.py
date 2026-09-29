class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toArr(s: str) -> List[int]:
            arr = [0] * 26
            for i in s:
                arr[ord(i) - ord('a')] += 1
            return arr
        
        my_map = defaultdict(list)
        for s in strs:
            my_map[tuple(toArr(s))].append(s)
        return list(my_map.values())