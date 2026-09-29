# neetcodeislove -> 0(n)
# neetcodeneet -> 4 (c)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = defaultdict(int)
        for idx, char in enumerate(s):
            map[char] += 1
        
        for idx, char in enumerate(s):
            if map[char] == 1:
                return idx
        return -1