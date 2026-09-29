class Solution:
    def validPalindrome(self, s: str) -> bool:
        for p in range(len(s)):
            l, r = 0, len(s) - 1

            while l < r:
                if l == p:
                    l += 1
                if r == p:
                    r -= 1
                
                if s[l] != s[r]: break
                else:
                    l += 1
                    r -= 1
            if l >= r: return True
        return False

        