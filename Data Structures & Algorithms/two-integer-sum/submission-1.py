class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 2):
            return [0, 1]

        map = dict()
        for i, v in enumerate(nums):
            if target - v in map:
                return [map[target - v], i]
            map[v] = i
        return [0, 0]