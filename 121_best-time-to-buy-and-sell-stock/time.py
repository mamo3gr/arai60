"""min,maxとif,elifとでパフォーマンスの差を計測するコード"""

import timeit
import random
import itertools


def max_profit_min_max(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


def max_profit_if(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
            continue
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit


def max_profit_itertools(prices):
    if not prices:
        return 0
    min_prices = itertools.accumulate(prices, min)
    profits = (price - min_p for price, min_p in zip(prices, min_prices))
    return max(profits)


# テストデータ (10万件)
data = [random.randint(1, 10000) for _ in range(10**5)]
iterations = 1000

# 計測
t_min_max = timeit.timeit(lambda: max_profit_min_max(data), number=iterations)
t_if = timeit.timeit(lambda: max_profit_if(data), number=iterations)
t_iter = timeit.timeit(lambda: max_profit_itertools(data), number=iterations)

print(f"--- 実行結果 (データ数: 100,000, 試行回数: {iterations}) ---")
print(f"min/max:   {t_min_max:.4f} 秒")
print(f"if:        {t_if:.4f} 秒")
print(f"Itertools: {t_iter:.4f} 秒")
