import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        分割統治法による実装。
        中央をまたぐ場合の探索が煩雑。左端を延ばしたときに、右端を縮められるかチェックが必要で、
        それぞれのタイミングで最小値を更新できるかチェックしないといけない。

        inspired from:
        https://github.com/naoto-iwase/leetcode/pull/50/changes#r2505036369
        """
        def helper(start: int, last: int) -> int:
            if last < start:
                return math.inf
            if start == last:
                return 1 if nums[start] >= target else math.inf

            mid = start + (last - start) // 2
            left_min = helper(start, mid)
            right_min = helper(mid + 1, last)
            crossing_mid_min = min_subarray_length_crossing_mid(start, last, mid)
            return min(left_min, right_min, crossing_mid_min)

        def min_subarray_length_crossing_mid(start: int, last: int, mid: int) -> int:
            min_length = math.inf
            left = mid
            right = mid + 1
            total = nums[left] + nums[right]
            if total >= target:
                return 2

            while start <= left:
                while total < target and right < last:
                    right += 1
                    total += nums[right]

                if total >= target:
                    length = right - left + 1
                    min_length = min(min_length, length)

                left -= 1
                if left < start:
                    break
                total += nums[left]

                while total > target and mid + 1 <= right:
                    total -= nums[right]
                    right -= 1
                    if total >= target:
                        length = right - left + 1
                        min_length = min(min_length, length)

            return min_length

        min_length = helper(0, len(nums) - 1)
        if min_length == math.inf:
            return 0
        return min_length
