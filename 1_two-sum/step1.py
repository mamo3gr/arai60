class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()  # key: number, value: index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [i, seen.get(complement)]
            else:
                seen[n] = i
