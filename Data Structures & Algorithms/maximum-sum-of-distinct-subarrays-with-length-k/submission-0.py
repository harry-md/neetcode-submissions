class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        counter = defaultdict(int)
        for i in range(k):
            counter[nums[i]] += 1
        cur_sum = sum(nums[:k])
        res = cur_sum if len(counter) == k else 0

        for i in range(k, len(nums)):
            left, right = nums[i - k], nums[i]
            if left == right:
                continue

            cur_sum += right - left

            counter[left] -= 1
            if counter[left] == 0:
                counter.pop(left)

            counter[right] += 1

            if len(counter) == k:
                res = max(res, cur_sum)
        return res