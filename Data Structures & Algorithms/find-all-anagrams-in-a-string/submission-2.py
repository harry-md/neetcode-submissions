class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        if len(s) < n:
            return []

        res = []
        target = Counter(p)
        window = Counter(s[:n])
        if window == target:
            res.append(0)

        for i in range(n, len(s)):
            l, r = s[i - n], s[i]

            window[l] -= 1
            if window[l] == 0:
                window.pop(l)

            window[r] += 1

            if window == target:
                res.append(i - n + 1)
        return res
