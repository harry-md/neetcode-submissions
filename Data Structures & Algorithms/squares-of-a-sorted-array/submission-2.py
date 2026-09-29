class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = -1
        for idx, num in enumerate(nums):
            if num >= 0:
                r = idx
                break

        nums = [num ** 2 for num in nums]
        res = []

        r = len(nums) if r == -1 else r
        l = r - 1

        while l >= 0 and r < len(nums):
            if nums[l] < nums[r]:
                res.append(nums[l])
                l -= 1
            else:
                res.append(nums[r])
                r += 1
        
        while l >= 0:
            res.append(nums[l])
            l -= 1
        while r < len(nums):
            res.append(nums[r])
            r += 1
        return res