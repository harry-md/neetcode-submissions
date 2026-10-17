class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        count = 0

        vowels = set("ueoai")
        for i in range(k):
            if s[i] in vowels:
                count += 1

        tmp = count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                tmp -= 1
            if s[i] in vowels:
                tmp += 1
            count = max(count, tmp)
        return count