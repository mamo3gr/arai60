class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_to_index:
                return [i, num_to_index.get(complement)]
            else:
                num_to_index[n] = i
