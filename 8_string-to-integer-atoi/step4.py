class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        s_i = 0
        while s_i < len(s) and s[s_i] == " ":
            s_i += 1

        if s_i >= len(s):
            return 0

        is_minus = False
        if s[s_i] == "-":
            is_minus = True
            s_i += 1
        elif s[s_i] == "+":
            s_i += 1

        if s_i >= len(s):
            return 0

        while s_i < len(s) and s[s_i] == "0":
            s_i += 1

        integer = 0
        limit = INT_MAX // 10
        last_digit_limit = INT_MAX % 10
        for c in s[s_i:]:
            if not "0" <= c <= "9":
                break
            digit = ord(c) - ord("0")
            overflow = integer > limit or (
                integer == limit and digit > last_digit_limit
            )
            if overflow:
                return INT_MIN if is_minus else INT_MAX
            integer = integer * 10 + digit

        if is_minus:
            integer *= -1
        return integer
