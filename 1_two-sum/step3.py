class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            raise ValueError(f"Array size ({len(nums)}) must be more than two.")

        num_to_index = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_to_index:
                return [i, num_to_index[complement]]
            else:
                num_to_index[n] = i

        raise ValueError("No pair found.")
