# r: a | m: a -> True
# r: ab | m: abcd -> True
# r: a | m: bbaa -> False
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for i in ransomNote:
            counter[i] -= 1
            if counter[i] < 0:
                return False
        return True
        