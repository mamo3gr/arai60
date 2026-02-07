import math


class Solution:
    MAX_WEIGHT_PER_PACKAGE = 500

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        lower = sum(weights) // days
        upper = self.MAX_WEIGHT_PER_PACKAGE * math.ceil(len(weights) / days)
        while lower < upper:
            middle = lower + (upper - lower) // 2
            if self.is_shipped_within_days(weights, days, middle):
                upper = middle
            else:
                lower = middle + 1

        return lower

    @staticmethod
    def is_shipped_within_days(weights: list[int], days: int, capacity: int) -> bool:
        loading = 0
        days_passed = 1
        for weight in weights:
            if weight > capacity:
                return False

            if loading + weight > capacity:
                days_passed += 1
                loading = 0
            loading += weight

        return days_passed <= days
