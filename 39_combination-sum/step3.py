class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []

        candidates = sorted(candidates)

        def generate_combinations_from(
            start: int, combination: list[int], target: int
        ) -> None:
            if target == 0:
                all_combinations.append(combination.copy())

            for i in range(start, len(candidates)):
                num = candidates[i]
                if target < num:
                    break
                combination.append(num)
                generate_combinations_from(i, combination, target - num)
                combination.pop()

        generate_combinations_from(start=0, combination=[], target=target)
        return all_combinations
