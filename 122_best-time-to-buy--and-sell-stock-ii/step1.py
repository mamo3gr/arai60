class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = prices[0]
        total_profit = 0

        for price in prices:
            if price < hold:
                hold = price
                continue

            profit = price - hold
            if profit > 0:
                total_profit += profit
                hold = price

        return total_profit
