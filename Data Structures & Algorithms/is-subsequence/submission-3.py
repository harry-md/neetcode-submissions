class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)

        if s_len == 0: return True
        if s_len > t_len: return False

        ps, pt = 0, 0
        while ps < s_len and pt < t_len:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        return ps == s_len
        