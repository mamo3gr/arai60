class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []

        combination = []
        total = 0

        def append_to_combination(i: int):
            nonlocal total

            if i >= len(candidates):
                return

            n = candidates[i]
            num_appends = 0
            while total < target:
                combination.append(n)
                total += n
                num_appends += 1

            if total == target:
                all_combinations.append(combination.copy())

            for _ in range(num_appends):
                combination.pop()
                total -= n
                append_to_combination(i + 1)

        append_to_combination(0)
        return all_combinations
