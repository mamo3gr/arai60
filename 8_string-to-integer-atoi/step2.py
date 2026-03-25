class Solution:
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    def myAtoi(self, s: str) -> int:
        def skip_leading_zeroes(s: str) -> int:
            i = 0
            while i < len(s) and s[i] == " ":
                i += 1
            return i

        def find_number_range(s: str, start: int) -> tuple[int, int]:
            while start < len(s) and s[start] == "0":
                start += 1
            end = start
            while end < len(s) and ord("0") <= ord(s[end]) <= ord("9"):
                end += 1
            return start, end

        i = skip_leading_zeroes(s)
        if i == len(s):
            return 0
        is_minus = s[i] == "-"
        if is_minus or s[i] == "+":
            i += 1

        start, end = find_number_range(s, i)
        if end - start <= 0:
            return 0
        num = int(s[start:end])
        if is_minus:
            num = -num

        num = max(num, self.INT_MIN)
        num = min(num, self.INT_MAX)

        return num
