class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_count, count = 0, 0
        for num in nums:
            if num == 1:
                cur_count += 1
            else:
                cur_count = 0

            if cur_count > count:
                count = cur_count
        return count