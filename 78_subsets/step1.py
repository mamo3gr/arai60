class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets: list[list[int]] = []

        fixed: list[int] = []
        remaining = nums.copy()
        frontier = [(fixed, remaining)]
        while frontier:
            fixed, remaining = frontier.pop()
            if not remaining:
                all_subsets.append(fixed)
                continue
            frontier.append((fixed + [remaining[0]], remaining[1:]))
            frontier.append((fixed.copy(), remaining[1:]))

        return all_subsets
