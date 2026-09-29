class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                for j in range(i + 1, n):
                    nums[i] = nums[j]
                n -= 1
                k += 1
            else:
                i += 1
        return i