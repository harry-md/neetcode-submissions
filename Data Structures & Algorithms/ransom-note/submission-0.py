# r: a | m: a -> True
# r: ab | m: abcd -> True
# r: a | m: bbaa -> False
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        ransome_note_freq = [0] * 26
        magazine_freq = [0] * 26
        a = ord('a')
        for i in ransomNote:
            ransome_note_freq[ord(i) - 97] += 1
        
        for i in magazine:
            ransome_note_freq[ord(i) - 97] -= 1
        
        for i in ransome_note_freq:
            if i > 0:
                return False
        return True

        