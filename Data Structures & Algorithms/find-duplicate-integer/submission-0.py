class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for num, freq in counter.items():
            if freq != 1:
                return num
        