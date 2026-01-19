class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def find_max_sum_in_range(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_max = find_max_sum_in_range(left, mid)
            right_max = find_max_sum_in_range(mid + 1, right)
            mid_max = find_max_sum_crossing_mid(left, right, mid)
            return max(left_max, right_max, mid_max)

        def find_max_sum_crossing_mid(left: int, right: int, mid: int) -> int:
            leftward_sum = 0
            left_max = nums[mid]
            for i in range(mid, left - 1, -1):
                leftward_sum += nums[i]
                left_max = max(left_max, leftward_sum)

            rightward_sum = 0
            right_max = nums[mid + 1]
            for i in range(mid + 1, right + 1):
                rightward_sum += nums[i]
                right_max = max(right_max, rightward_sum)

            return left_max + right_max

        return find_max_sum_in_range(0, len(nums) - 1)
