class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                c = nums[i] + nums[l] + nums[r]
                if c == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l, r = l + 1, r - 1
                elif c < 0:
                    l += 1
                else:
                    r -= 1

        return [list(i) for i in res]