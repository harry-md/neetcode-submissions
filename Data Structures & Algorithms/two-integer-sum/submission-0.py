class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 2):
            return [0, 1]

        map = dict()
        for i, value in enumerate(nums):
            if (target - value) in map:
                return [map[target - value], i]
            map[value] = i
        return [0, 0]