class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_to_count = defaultdict(int, {0: 1})
        count = 0

        for i, n in enumerate(nums):
            prefix_sum += n
            complement = prefix_sum - k
            count += prefix_sum_to_count.get(complement, 0)
            prefix_sum_to_count[prefix_sum] += 1

        return count
