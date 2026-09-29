class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        
        while fast < len(chars):
            count = 0
            char = chars[fast]

            while fast < len(chars) and char == chars[fast]:
                count += 1
                fast += 1
            
            chars[slow] = char
            slow += 1

            if count >= 2:
                for digit in str(count):
                    chars[slow] = digit
                    slow += 1
        return slow

        