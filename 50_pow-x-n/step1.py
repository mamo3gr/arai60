import functools


class Solution:
    @functools.cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        negative = False
        if n < 0:
            negative = True
            n *= -1

        if n % 2 == 0:
            pow = self.myPow(x, n // 2) * self.myPow(x, n // 2)
        else:
            pow = self.myPow(x, n // 2) * self.myPow(x, n // 2) * x

        if negative:
            return 1 / pow
        else:
            return pow
