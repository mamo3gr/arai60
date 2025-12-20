class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue

            if len(stack) == 0:
                return False

            last_pushed = stack.pop()
            if last_pushed == '(' and char == ')':
                pass
            elif last_pushed == '{' and char == '}':
                pass
            elif last_pushed == '[' and char == ']':
                pass
            else:
                return False

        if len(stack) > 0:
            return False

        return True
