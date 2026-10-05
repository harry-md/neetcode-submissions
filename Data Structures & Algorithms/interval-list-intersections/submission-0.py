class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len1, len2 = len(firstList), len(secondList)
        if len1 == 0 or len2 == 0:
            return []

        res = []

        start = min(firstList[0][0], secondList[0][0])
        end = max(firstList[len1 - 1][1], secondList[len2 - 1][1])
        i, j = 0, 0
        p = start
        while p <= end and i < len1 and j < len2: 
            if firstList[i][0] <= p and secondList[j][0] <= p:
                s = p
                while p <= firstList[i][1] and p <= secondList[j][1]:
                    p += 1
                res.append([s, p - 1])
            else:
                p += 1
            
            if p > firstList[i][1]:
                i += 1
            if p > secondList[j][1]:
                j += 1
        return res