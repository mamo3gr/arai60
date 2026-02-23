import functools
import itertools


class Solution:
    @functools.cache
    def generateParenthesis(self, n: int) -> list[str]:
        """
        (A)B という形に分け、AとBを n-1 までの結果から列挙するパターン。

        inspired from:
        https://github.com/olsen-blue/Arai60/pull/54#discussion_r2027288220
        """
        if n == 0:
            return [""]

        all_parentheses = []
        for i in range(n):
            for A, B in itertools.product(
                self.generateParenthesis(i), self.generateParenthesis(n - 1 - i)
            ):
                all_parentheses.append(f"({A}){B}")

        return all_parentheses
