class Solution:
    def countWays(self, n, k):
        # the number of ways where the last two posts' color are the same / different
        tail_consecutive = 0
        tail_different = k

        for _ in range(1, n):
            new_tail_consecutive = tail_different
            new_tail_different = (tail_different + tail_consecutive) * (k - 1)

            tail_consecutive = new_tail_consecutive
            tail_different = new_tail_different

        return tail_consecutive + tail_different

    def countWaysReccurenceFormula(self, n, k):
        """
        漸化式 T_i = (k-1)(T_{i-1} + T_{i-2}) を利用するパターン。
        これも空間計算量を O(1) にできるが、漸化式との対応の分かりやすさのため
        意図的にそうしていない。

        inspired from:
        https://github.com/naoto-iwase/leetcode/pull/35
        """
        if n == 1:
            return k

        num_ways = [0] * (n + 1)
        num_ways[1] = k
        num_ways[2] = k * k

        for i in range(3, n + 1):
            num_ways[i] = (k - 1) * (num_ways[i - 1] + num_ways[i - 2])

        return num_ways[-1]
