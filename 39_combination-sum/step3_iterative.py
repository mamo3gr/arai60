class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []

        combination = []
        candidate_i = 0
        frontier = [(combination, candidate_i, target)]
        while frontier:
            combination, candidate_i, target = frontier.pop()
            if target == 0:
                all_combinations.append(combination.copy())
                continue

            if candidate_i >= len(candidates):
                continue

            num = candidates[candidate_i]
            while target >= 0:
                frontier.append((combination.copy(), candidate_i + 1, target))
                combination.append(num)
                target -= num

        return all_combinations
