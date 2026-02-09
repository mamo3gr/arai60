class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)

        powered = 1
        testing_bit = 1
        cumulated_product = x
        while testing_bit <= n:
            if n & testing_bit:
                powered *= cumulated_product
            cumulated_product *= cumulated_product
            testing_bit <<= 1

        return powered
