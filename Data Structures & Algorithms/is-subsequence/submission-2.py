class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)

        if s_len == 0: return True
        if s_len > t_len: return False

        p1, p2 = 0, 0
        done = False
        while p1 < s_len and p2 < t_len:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
                if p1 == s_len:
                    done = True
            else:
                p2 += 1
        return done
        