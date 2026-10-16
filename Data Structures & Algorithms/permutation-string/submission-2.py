class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        n = len(s1)

        for i in range(len(s2) - n + 1):
            if s2[i] in counter:
                tmp = counter.copy()
                tmp[s2[i]] -= 1
                if tmp[s2[i]] == 0:
                    tmp.pop(s2[i])
                
                j = i + 1
                while j < len(s2) and j < i + n and s2[j] in tmp:
                    tmp[s2[j]] -= 1

                    if tmp[s2[j]] == 0:
                        tmp.pop(s2[j])
                    j+=1
                if j == i + n:
                    return True
        return False
