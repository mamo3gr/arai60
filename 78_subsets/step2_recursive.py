class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        再帰と反復による実装。

        inspired from:
        https://github.com/garunitule/coding_practice/pull/51
        """

        def generate_subsets_from(start: int):
            if start >= len(nums):
                return [[]]

            child_subsets = generate_subsets_from(start + 1)
            return child_subsets + [subset + [nums[start]] for subset in child_subsets]

        return generate_subsets_from(0)
