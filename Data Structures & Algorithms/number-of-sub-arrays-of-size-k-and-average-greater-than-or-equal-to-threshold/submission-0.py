class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        cur_sum = sum(arr[:k])
        target_sum = threshold * k

        if cur_sum >= target_sum:
            count += 1

        for i in range(k, len(arr)):
            cur_sum += arr[i] - arr[i - k]
            if cur_sum >= target_sum:
                count += 1

        return count