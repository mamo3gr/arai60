class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        min_capacity = max(weights)  # days日で出荷する
        max_capacity = sum(weights)  # 1日で出荷する
        while min_capacity < max_capacity:
            mid_capacity = min_capacity + (max_capacity - min_capacity) // 2
            if self.compute_shipping_days(weights, mid_capacity) <= days:
                max_capacity = mid_capacity
            else:
                min_capacity = mid_capacity + 1

        return min_capacity

    @staticmethod
    def compute_shipping_days(weights: list[int], capacity: int) -> int:
        days = 1
        loading = 0
        for weight in weights:
            if loading + weight > capacity:
                days += 1
                loading = 0
            loading += weight
        return day
