class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        min = math.inf
        for idx, num in enumerate(nums):
            if num in hashmap:
                if abs(hashmap[num] - idx) < min:
                    min = abs(hashmap[num] - idx)
                    hashmap[num] = idx
            else:
                hashmap[num] = idx
        return True if min <= k else False