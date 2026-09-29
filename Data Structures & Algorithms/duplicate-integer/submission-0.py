class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set(nums)
        return len(ans) != len(nums)