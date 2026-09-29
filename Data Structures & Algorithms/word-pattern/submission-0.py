class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        mp = {}
        seen_words = set()

        for idx, char in enumerate(pattern):
            if char in mp:
                if mp[char] != words[idx]:
                    return False
            else:
                if words[idx] in seen_words:
                    return False
            mp[char] = words[idx]
            seen_words.add(words[idx])
        return True