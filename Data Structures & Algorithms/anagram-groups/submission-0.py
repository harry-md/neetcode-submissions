class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toArr(s) -> List[int]:
            arr = [0] * 26
            for i in s:
                arr[ord(i) - ord('a')] += 1
            return arr

        dictionary = defaultdict(list)
        for s in strs:
            dictionary[tuple(toArr(s))].append(s)
        return list(dictionary.values())