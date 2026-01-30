import collections


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        BFS
        """
        frontier = collections.deque([(0, 0)])
        visited = set()
        while frontier:
            total, num_coins = frontier.popleft()
            if total == amount:
                return num_coins

            for coin in coins:
                next_total = total + coin
                if next_total > amount:
                    continue
                if next_total in visited:
                    continue
                frontier.append((next_total, num_coins + 1))
                visited.add(next_total)

        return -1
