class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # minimum coins to make up i
        sentinel = [0]
        min_coins = sentinel + [-1] * amount

        for target in range(1, amount + 1):
            # to fill min_coins[target]
            min_coins_target = math.inf
            for coin in coins:
                complement = target - coin
                if complement < 0:
                    continue
                if min_coins[complement] == -1:
                    continue
                if min_coins[complement] + 1 < min_coins_target:
                    min_coins_target = min_coins[complement] + 1

            if min_coins_target != math.inf:
                min_coins[target] = min_coins_target

        return min_coins[-1]
