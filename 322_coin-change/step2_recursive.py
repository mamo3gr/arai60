import functools
import math


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        再帰＋メモ化での実装。
        特に再帰であるメリットは感じなかったが、選択肢の幅として書いてみた。
        """

        @functools.cache
        def compute_min_coins(target: int) -> int:
            if target < 0:
                return -1
            if target == 0:
                return 0

            min_coins = math.inf
            for coin in coins:
                new_target = target - coin
                num_coins = compute_min_coins(new_target)
                if num_coins == -1:
                    continue
                if num_coins + 1 < min_coins:
                    min_coins = num_coins + 1

            if min_coins == math.inf:
                return -1
            else:
                return min_coins

        return compute_min_coins(amount)
