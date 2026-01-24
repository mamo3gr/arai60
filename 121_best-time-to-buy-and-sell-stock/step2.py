import itertools


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_prices = itertools.accumulate(prices, min)
        profits = [price - min_price for price, min_price in zip(prices, min_prices)]
        return max(profits)
