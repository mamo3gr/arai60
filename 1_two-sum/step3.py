class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            raise ValueError(f"Array size ({len(nums)}) must be more than two.")

        num_to_target = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_to_target:
                return [i, num_to_target[complement]]
            else:
                num_to_target[n] = i

        raise ValueError("No pair found.")
