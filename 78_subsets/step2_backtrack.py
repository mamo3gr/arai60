class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        バックトラッキングによる実装
        """
        all_subsets = []

        subset = []

        def generate_subsets_from(start: int):
            all_subsets.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])
                generate_subsets_from(i + 1)
                subset.pop()

        generate_subsets_from(0)
        return all_subsets

    def subsetsBinaryTree(self, nums: list[int]) -> list[list[int]]:
        """
        バックトラッキングによる実装。
        nums[i] を入れる・入れない場合というバイナリツリー型。
        """
        all_subsets = []

        subset = []

        def generate_subsets_from(position: int):
            if position >= len(nums):
                all_subsets.append(subset.copy())
                return

            subset.append(nums[position])
            generate_subsets_from(position + 1)

            subset.pop()
            generate_subsets_from(position + 1)

        generate_subsets_from(0)
        return all_subsets
