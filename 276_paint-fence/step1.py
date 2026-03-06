class Solution:
    def countWays(self, n, k):
        count_ways = [0] + [None] * n
        num_tail_two_consecutive = [0] * (n + 1)

        count_ways[1] = k
        num_tail_two_consecutive[1] = 0
        for i in range(2, n + 1):
            num_tail_two_consecutive[i] = (
                count_ways[i - 1] - num_tail_two_consecutive[i - 1]
            )
            count_ways[i] = count_ways[i - 1] * k - num_tail_two_consecutive[i - 1]

        return count_ways[-1]
