class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRACKETS = ('(', '{', '[')
        open_to_close = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        for char in s:
            if char in OPEN_BRACKETS:
                stack.append(char)
                continue

            try:
                last_pushed = stack.pop()
            except IndexError:
                return False
            
            if open_to_close[last_pushed] == char:
                pass
            else:
                return False
        
        return len(stack) == 0
