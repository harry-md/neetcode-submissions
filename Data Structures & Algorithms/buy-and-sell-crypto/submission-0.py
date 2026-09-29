class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        minPrice = prices[0]
        diff = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > diff:
                diff = price - minPrice
        return diff if diff > 0 else 0