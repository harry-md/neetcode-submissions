class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        # while idx < len(nums):
        #     if nums[k] == nums[idx]:
        #         idx += 1
        #     else:
        #         k += 1
        #         nums[k] = nums[idx]
        #         idx += 1
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1
        
        