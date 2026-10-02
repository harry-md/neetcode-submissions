class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3

        for num in nums:
            bucket[num] += 1
        
        idx = 0

        for slot, val in enumerate(bucket):
            for i in range(val):
                nums[idx] = slot
                idx += 1
        
        