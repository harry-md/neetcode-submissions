class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0

        while fast < len(chars):
            count = 1
            char_at_fast = chars[fast]

            while fast + 1 < len(chars) and chars[fast + 1] == char_at_fast:
                count += 1
                fast += 1
            fast += 1
            
            chars[slow] = char_at_fast
            slow += 1
            
            if count > 1:
                for digit in str(count):
                    chars[slow] = digit
                    slow += 1
        return slow