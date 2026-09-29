# neetcodeislove -> 0(n)
# neetcodeneet -> 4 (c)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = defaultdict(int)
        for idx, char in enumerate(s):
            map[char] += 1
        
        for key, value in map.items():
            if value == 1:
                return s.find(key)
        return -1

        

        