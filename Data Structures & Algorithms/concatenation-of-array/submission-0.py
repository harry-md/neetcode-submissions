class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [None] * 2 * length
        for idx, value in enumerate(nums):
            ans[idx] = value
            ans[idx + length] = value
        return ans