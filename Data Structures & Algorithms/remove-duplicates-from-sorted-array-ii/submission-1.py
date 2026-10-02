class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s, f = 0, 0

        while f < len(nums):
            fast = nums[f]
            count = 1
            
            while f + 1 < len(nums) and nums[f + 1] == fast:
                f += 1
                count += 1
            f += 1
            
            for i in range(min(count, 2)):
                nums[s] = fast
                s += 1
        return s
        