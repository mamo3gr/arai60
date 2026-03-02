class Solution:
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        if i == len(s):
            return 0
        is_minus = s[i] == "-"
        if is_minus or s[i] == "+":
            i += 1

        num_start = i
        while num_start < len(s) and s[num_start] == "0":
            num_start += 1
        num_end = num_start
        while num_end < len(s) and ord("0") <= ord(s[num_end]) <= ord("9"):
            num_end += 1
        if num_end - num_start <= 0:
            return 0
        num = int(s[num_start:num_end])
        if is_minus:
            num = -num

        num = max(num, self.INT_MIN)
        num = min(num, self.INT_MAX)

        return num
