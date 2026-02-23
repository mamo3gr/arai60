class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        all_parentheses = []

        def generate_parentheses(
            parenthesis: list[str], num_opens: int, num_closes: int
        ) -> None:
            if num_opens == num_closes == n:
                all_parentheses.append("".join(parenthesis))
                return

            if num_opens < n:
                parenthesis.append("(")
                generate_parentheses(parenthesis, num_opens + 1, num_closes)
                parenthesis.pop()

            if num_closes < num_opens:
                parenthesis.append(")")
                generate_parentheses(parenthesis, num_opens, num_closes + 1)
                parenthesis.pop()

        generate_parentheses(parenthesis=[], num_opens=0, num_closes=0)
        return all_parentheses
