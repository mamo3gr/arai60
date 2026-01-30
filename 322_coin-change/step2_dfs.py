import math


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins_descending = sorted(coins, reverse=True)
        min_coins = [math.inf] * (amount + 1)
        best = math.inf
        frontier = [(0, 0, 0)]  # (total, num_coins, coin_index)
        while frontier:
            total, num_coins, coin_i = frontier.pop()
            if num_coins >= best:
                continue
            if total == amount:
                best = min(best, num_coins)
                continue
            if len(coins_descending) <= coin_i:
                continue

            coin = coins_descending[coin_i]

            remaining = amount - total
            min_possible = num_coins + math.ceil(remaining / coin)
            if min_possible >= best:
                continue

            # このコインを使う
            new_total = total + coin
            new_num_coins = num_coins + 1
            if new_total <= amount and new_num_coins < min_coins[new_total]:
                min_coins[new_total] = new_num_coins
                frontier.append((new_total, new_num_coins, coin_i))

            # このコインを使わない（次のコインを使う）
            frontier.append((total, num_coins, coin_i + 1))

        return best if best != math.inf else -1
