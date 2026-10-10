class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set = set(nums)
        res = 0

        for num in _set:
            if num - 1 not in _set:
                tmp = num
                count = 0
                while tmp in _set:
                    count += 1
                    tmp += 1
                res = max(res, count)
        return res