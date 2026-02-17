class Solution:
    def permuteStack(self, nums: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = []
        fixed = []
        remaining = nums.copy()
        frontier = [(fixed, remaining)]
        while frontier:
            fixed, remaining = frontier.pop()

            if len(fixed) == len(nums):
                permutations.append(fixed)
                continue

            for r in remaining:
                fixed_new = fixed + [r]
                remaining_new = remaining.copy()
                remaining_new.remove(r)
                frontier.append((fixed_new, remaining_new))

        return permutations

    def permuteSwap(self, nums: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = []
        n = len(nums)

        def permute_from(start: int):
            if start == n:
                permutations.append(nums.copy())

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                permute_from(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        permute_from(0)
        return permutations

    def permuteSet(self, nums: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = []
        not_used = set(nums)
        fixed = []

        def pick_and_delegate_rest(not_used: set[int], fixed: list[int]):
            if len(fixed) == len(nums):
                permutations.append(fixed.copy())
                return

            for num in list(not_used):
                fixed.append(num)
                not_used.remove(num)

                pick_and_delegate_rest(not_used, fixed)

                fixed.pop()
                not_used.add(num)

        pick_and_delegate_rest(not_used, fixed)
        return permutations
