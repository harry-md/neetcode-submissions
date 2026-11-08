class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        res = 0
        while i < len(nums):
            if nums[i] == 1:
                j, count = i, 0
                while j < len(nums) and nums[j] == 1:
                    count += 1
                    j += 1
                res = max(res, count)
                i = j + 1
            else:
                i += 1
        return res