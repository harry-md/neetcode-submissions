# [2, 3, 5, 2, 4]
# [2, 3, 2, 3, 2] -> [2, 2, 3, 3, 2]
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow =  0

        while slow < len(nums) and nums[slow] % 2 == 0:
            slow += 1
        
        for fast in range(slow + 1, len(nums)):
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums