class Solution:
    MAX_INT = (2**31) - 1
    MIN_INT = -(2**31)

    def myAtoi(self, s: str) -> int:
        def find_first_non_whitespace_char(s: str) -> int:
            i = 0
            while i < len(s) and s[i] == " ":
                i += 1
            return i

        def find_number_range(s: str, start: int) -> tuple[int, int]:
            end = start
            while end < len(s) and "0" <= s[end] <= "9":
                end += 1
            return start, end

        i = find_first_non_whitespace_char(s)
        if i == len(s):
            return 0

        is_minus = s[i] == "-"
        if is_minus or s[i] == "+":
            i += 1

        start, end = find_number_range(s, i)
        if end - start == 0:
            return 0
        num = int(s[start:end])
        if is_minus:
            num *= -1

        num = max(num, self.MIN_INT)
        num = min(num, self.MAX_INT)

        return num
