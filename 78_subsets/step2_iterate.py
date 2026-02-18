class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        反復による実装
        """
        all_subsets = [[]]
        for num in nums:
            all_subsets += [subset + [num] for subset in all_subsets]
        return all_subsets
