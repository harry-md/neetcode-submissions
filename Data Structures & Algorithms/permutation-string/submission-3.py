class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        
        s1_counter = defaultdict(int)
        s2_counter = defaultdict(int)
        
        for i in range(n):
            s1_counter[s1[i]] += 1
            s2_counter[s2[i]] += 1
        
        if s1_counter == s2_counter:
            return True
        
        for i in range(n, len(s2)):
            left, right = s2[i-n], s2[i]
            s2_counter[left] -= 1
            if s2_counter[left] == 0:
                s2_counter.pop(left)
            
            s2_counter[right] += 1

            if s1_counter == s2_counter:
                return True
        return False

