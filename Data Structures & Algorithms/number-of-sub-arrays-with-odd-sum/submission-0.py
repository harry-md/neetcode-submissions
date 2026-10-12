class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res, even, odd, cur = 0, 0, 0, 0

        for num in arr:
            cur += num

            if cur % 2 == 0:
                even += 1
                res += odd
            else:
                odd += 1
                res += 1 + even
        return res