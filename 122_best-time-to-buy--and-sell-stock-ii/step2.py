import itertools


class Solution:
    def maxProfitItertoolsPairwise(self, prices: list[int]) -> int:
        """
        itertools.pairwiseを使って関数型っぽく。
        inspired from https://github.com/tshimosake/arai60/pull/22/changes#r2659438463
        """
        return sum(
            max(0, today - yesterday) for yesterday, today in itertools.pairwise(prices)
        )

    def maxProfitDP(self, prices: list[int]) -> int:
        """
        2状態DP
        inspired from https://github.com/tshimosake/arai60/pull/22
        """
        profit_without_stock = 0
        profit_holding_stock = -prices[0]

        for i in range(1, len(prices)):
            next_profit_without_stock = max(
                profit_without_stock,  # no operation
                profit_holding_stock + prices[i]  # sell
            )
            next_profit_holding_stock = max(
                profit_holding_stock,  # no operation
                profit_without_stock - prices[i]  # buy
            )
            profit_without_stock = next_profit_without_stock
            profit_holding_stock = next_profit_holding_stock

        return profit_without_stock

    def maxProfitFindingValleyAndPeak(self, prices: list[int]) -> int:
        """
        while文で谷を探して買い、山を探して売る。
        inspired from https://github.com/garunitule/coding_practice/pull/38
        """
        max_days = len(prices) - 1
        today = 0
        profit = 0

        while today < max_days:
            while today < max_days and prices[today] >= prices[today + 1]:
                today += 1
            buy = prices[today]

            while today < max_days and prices[today] <= prices[today + 1]:
                today += 1
            sell = prices[today]

            profit += sell - buy

        return profit
