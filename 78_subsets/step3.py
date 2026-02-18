class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        部下に仕事を与えて成果物を受け取り、自分の仕事をして返す、
        というイメージが一番想像しやすい。
        """

        def generate_subsets_from(start: int) -> list[list[int]]:
            if start >= len(nums):
                return [[]]

            child_subsets = generate_subsets_from(start + 1)
            return child_subsets + [subset + [nums[start]] for subset in child_subsets]

        return generate_subsets_from(0)

    def subsetsBinary(self, nums: list[int]) -> list[list[int]]:
        """
        nums[i] を入れる・入れないでバックトラックする、
        という考え方から比較的しっくりくる。
        """
        all_subsets: list[list[int]] = []

        subset = []

        def generate_subsets_from(i: int):
            if i >= len(nums):
                all_subsets.append(subset.copy())
                return

            subset.append(nums[i])
            generate_subsets_from(i + 1)

            subset.pop()
            generate_subsets_from(i + 1)

        generate_subsets_from(0)
        return all_subsets
