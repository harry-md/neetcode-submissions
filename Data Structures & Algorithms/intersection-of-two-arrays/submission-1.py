class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        res = set()
        for i in nums1:
            set1.add(i)
            if i in nums2 and i in set1:
                res.add(i)
        return list(res)