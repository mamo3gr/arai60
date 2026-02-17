import copy


class Solution:
    def permuteSwap(self, nums: list[int]) -> list[list[int]]:
        """
        swapによるバックトラッキング。
        Geminiに教えてもらったコードを自分なりに書き換えてみたもの
        """
        permutations: list[list[int]] = []
        n = len(nums)

        def permute_from(start: int):
            if start == n:
                fixed = copy.deepcopy(nums)
                permutations.append(fixed)

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                permute_from(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        permute_from(0)
        return permutations

    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        使用済みフラグを使ったバックトラッキング。

        inspired from:
        https://github.com/huyfififi/coding-challenges/pull/44/changes#r2693577983
        """
        permutations: list[list[int]] = []
        used = [False] * len(nums)
        fixed = []

        def pick_and_delegate_rest(used: list[bool], fixed: list[int]):
            if len(fixed) == len(nums):
                permutations.append(fixed.copy())
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue

                fixed.append(num)
                used[i] = True

                pick_and_delegate_rest(used, fixed)

                fixed.pop()
                used[i] = False

        pick_and_delegate_rest(used, fixed)
        return permutations

    def permuteNotUsedSet(self, nums: list[int]) -> list[list[int]]:
        """
        未使用の整数をsetで管理するバックトラッキング。

        inspired from:
        https://github.com/Ryotaro25/leetcode_first60/pull/54/changes/BASE..18a281be3c2a94e61417d2b03c7409a47d18ce31#r1986035628
        """
        permutations: list[list[int]] = []
        not_used = set(nums)
        fixed = []

        def pick_and_delegate_rest(not_used: set[int], fixed: list[int]):
            if len(fixed) == len(nums):
                permutations.append(fixed.copy())
                return

            # NOTE: イテレーションのたびに `not_used` の中身を動的に参照するので、
            # コピーしておく必要がある
            for num in list(not_used):
                fixed.append(num)
                not_used.remove(num)

                pick_and_delegate_rest(not_used, fixed)

                fixed.pop()
                not_used.add(num)

        pick_and_delegate_rest(not_used, fixed)
        return permutations
