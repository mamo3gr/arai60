class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        cumulative_sum_to_count = defaultdict(int, {0: 1})
        count = 0

        for i, n in enumerate(nums):
            total += n
            complement = total - k
            count += cumulative_sum_to_count.get(complement, 0)
            cumulative_sum_to_count[total] += 1

        return count
