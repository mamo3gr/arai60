class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        all_parenthesis = []

        frontier = [("", 0, 0)]
        while frontier:
            parenthesis, num_opens, num_closes = frontier.pop()
            if num_opens == num_closes == n:
                all_parenthesis.append(parenthesis)

            if num_opens < n:
                frontier.append((parenthesis + "(", num_opens + 1, num_closes))

            if num_closes < num_opens:
                frontier.append((parenthesis + ")", num_opens, num_closes + 1))

        return all_parenthesis
