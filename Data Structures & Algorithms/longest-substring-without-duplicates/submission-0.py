class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        l, n = 0, len(s)
        res = 0
        for r in range(n):
            right = s[r]

            while right in seen:
                left = s[l]
                seen[left] -= 1

                if seen[left] == 0:
                    seen.pop(left)
                l += 1

            seen[right] += 1
            res = max(res, r - l + 1)

        return res
