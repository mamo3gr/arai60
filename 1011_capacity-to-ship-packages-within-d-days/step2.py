import bisect


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_shipped_within_days(capacity: int) -> bool:
            days_passed = 1
            loaded = 0
            for weight in weights:
                if loaded + weight > capacity:
                    days_passed += 1
                    loaded = 0
                loaded += weight
            return days_passed <= days

        min_capacity = max(weights)
        max_capacity = sum(weights)
        return bisect.bisect_left(
            range(max_capacity + 1),
            True,
            key=is_shipped_within_days,
            lo=min_capacity,
        )
