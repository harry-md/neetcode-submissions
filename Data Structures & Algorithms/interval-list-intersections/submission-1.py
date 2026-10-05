class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        len1, len2 = len(firstList), len(secondList)
        if len1 == 0 or len2 == 0:
            return []

        res = []

        i, j = 0, 0
        while i < len1 and j < len2:
            a, b = firstList[i]
            c, d = secondList[j]

            s = max(a, c)
            e = min(b, d)
            if s <= e:
                res.append([s, e])

            if b < d:
                i += 1
            elif b > d:
                j += 1
            else:
                i += 1
                j += 1
        return res
