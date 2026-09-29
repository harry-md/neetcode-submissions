class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, idx = 0, 1
        while idx < len(nums):
            if nums[k] == nums[idx]:
                idx += 1
            else:
                k += 1
                nums[k] = nums[idx]
                idx += 1
        return k + 1
        
        