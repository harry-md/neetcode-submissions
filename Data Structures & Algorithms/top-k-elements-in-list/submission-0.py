class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = Counter(nums)
        
        res = []
        for i in range(k):
            t = max(my_map, key=my_map.get)
            res.append(t)
            my_map.pop(t)
        return res

