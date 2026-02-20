class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []

        candidates = sorted(candidates)

        def generate_combinations(
            start: int, target: int, combination: list[int]
        ) -> None:
            if target == 0:
                all_combinations.append(combination.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > target:
                    break
                combination.append(num)
                generate_combinations(i, target - num, combination)
                combination.pop()

        generate_combinations(0, target, [])
        return all_combinations
