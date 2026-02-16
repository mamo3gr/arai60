class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = []
        frontier: list[tuple[list[int], list[int]]] = [
            (
                [],
                list(range(len(nums))),
            )
        ]
        while frontier:
            fixed, remains = frontier.pop()
            if not remains:
                permuted = [nums[i] for i in fixed]
                permutations.append(permuted)
                continue

            for r in remains:
                frontier.append(
                    (
                        fixed + [r],
                        [i for i in remains if i != r],
                    )
                )

        return permutations
