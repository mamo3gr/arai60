class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        sentinel = [0]
        min_coins = sentinel + [math.inf] * amount

        for target in range(1, amount + 1):
            for coin in coins:
                base = target - coin
                if base < 0:
                    continue
                if min_coins[base] + 1 < min_coins[target]:
                    min_coins[target] = min_coins[base] + 1

        if min_coins[-1] == math.inf:
            return -1
        return min_coins[-1]
