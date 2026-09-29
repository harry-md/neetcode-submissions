class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        r = -1
        for idx, num in enumerate(nums):
            if num >= 0:
                r = idx
                break

        r = len(nums) if r == -1 else r
        l = r - 1

        while l >= 0 and r < len(nums):
            left = nums[l] ** 2
            right = nums[r] ** 2
            if left < right:
                res.append(left)
                l -= 1
            else:
                res.append(right)
                r += 1
        
        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            res.append(nums[r] ** 2)
            r += 1
        return res