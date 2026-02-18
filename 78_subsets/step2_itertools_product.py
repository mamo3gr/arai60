import itertools


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        itertools.productを用いた実装
        """
        choices = [(num, None) for num in nums]
        all_subsets = []
        # NOTE: 内包表記でも書けるが、可読性を重視して for 文で書く
        for combination in itertools.product(*choices):
            subset = [x for x in combination if x is not None]
            all_subsets.append(subset)

        return all_subsets
