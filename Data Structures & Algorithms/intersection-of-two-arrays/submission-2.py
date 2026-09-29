class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        seen = set(nums1)
        for i in nums2:
            if i in seen:
                res.append(i)
                seen.remove(i)
        return res