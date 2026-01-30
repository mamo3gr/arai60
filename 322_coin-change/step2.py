import math


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        coinを外側にしてみたバージョン。
        inspired from https://github.com/naoto-iwase/leetcode/pull/45
        """
        INF = amount + 1

        sentinel = [0]
        min_coins = sentinel + [INF] * amount

        for coin in coins:
            for target in range(coin, amount + 1):
                reminder = target - coin
                if min_coins[reminder] == INF:
                    continue

                min_coins[target] = min(
                    min_coins[target],
                    min_coins[reminder] + 1,
                )

        if min_coins[-1] == INF:
            return -1
        return min_coins[-1]

    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        coinsを昇順ソートして、早期にbreakするバージョン。
        inspired from https://github.com/naoto-iwase/leetcode/pull/45
        """
        INF = amount + 1

        sentinel = [0]
        min_coins = sentinel + [INF] * amount
        coins_ascending = sorted(coins)

        for target in range(1, amount + 1):
            for coin in coins_ascending:
                remainder = target - coin
                if remainder < 0:
                    break

                min_coins[target] = min(
                    min_coins[target],
                    min_coins[remainder] + 1,
                )

        if min_coins[-1] == INF:
            return -1
        return min_coins[-1]
