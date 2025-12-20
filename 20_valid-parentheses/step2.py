class Solution:
    @staticmethod
    def _brackets_matched(opening: str, closing: str) -> bool:
        if opening == '(' and closing == ')':
            return True
        elif opening == '{' and closing == '}':
            return True
        elif opening == '[' and closing == ']':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        BRACKETS_OPEN = ('(', '{', '[')
        stack = []
        for char in s:
            if char in BRACKETS_OPEN:
                stack.append(char)
                continue

            try:
                last_pushed = stack.pop()
            except IndexError:  # stack is empty
                return False

            if not self._brackets_matched(last_pushed, char):
                return False

        if len(stack) > 0:
            return False

        return True
