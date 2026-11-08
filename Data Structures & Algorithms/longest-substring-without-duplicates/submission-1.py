class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        l = 0
        res = 0
        for r, r_char in enumerate(s):
            while r_char in seen:
                seen[s[l]] -= 1

                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l += 1

            seen[r_char] += 1
            res = max(res, r - l + 1)

        return res
