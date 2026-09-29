class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                pl = l + 1
                pr = r
                while pl < pr:
                    if s[pl] == s[pr]:
                        pl += 1
                        pr -= 1
                    else: break
                if pl >= pr: return True
                
                pl = l
                pr = r - 1
                while pl < pr:
                    if s[pl] == s[pr]:
                        pl += 1
                        pr -= 1
                    else: break
                if pl >= pr: return True
                return False
        return l >= r