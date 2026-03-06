class Solution:
    def countWays(self, n, k):
        # number of ways where the last two posts' color are different / same
        tail_different = k
        tail_consecutive = 0

        for _ in range(1, n):
            new_tail_different = tail_different * (k - 1) + tail_consecutive * (k - 1)
            new_tail_consecutive = tail_different

            tail_different = new_tail_different
            tail_consecutive = new_tail_consecutive

        return tail_different + tail_consecutive
