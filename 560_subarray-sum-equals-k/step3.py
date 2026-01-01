class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_to_count = defaultdict(int, {0: 1})
        num_subarrays = 0
        for n in nums:
            prefix_sum += n
            complement = prefix_sum - k
            num_subarrays += prefix_sum_to_count[complement]
            prefix_sum_to_count[prefix_sum] += 1

        return num_subarrays
