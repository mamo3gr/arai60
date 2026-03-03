class Solution:
    def convert(self, s: str, numRows: int) -> str:
        num_rows = numRows
        lines = [[] for _ in range(num_rows)]

        row = 0
        going_down = True
        i = 0
        while i < len(s):
            lines[row].append(s[i])
            i += 1
            if going_down:
                row += 1
                if row >= num_rows - 1:
                    going_down = False
                row = min(row, num_rows - 1)
            else:
                row -= 1
                if row <= 0:
                    going_down = True
                row = max(row, 0)

        chars = []
        for line in lines:
            chars.extend(c for c in line)

        return "".join(chars)
