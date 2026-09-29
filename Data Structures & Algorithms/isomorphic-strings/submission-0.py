class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        seen_val = set()

        for idx, char in enumerate(s):
            if char in mp:
                if mp[char] != t[idx]:
                    return False
            else:
                if t[idx] in seen_val:
                    return False
                mp[char] = t[idx]
                seen_val.add(t[idx])
        return True