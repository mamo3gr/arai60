class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        row_index = 0
        direction = 1
        for c in s:
            rows[row_index].append(c)

            if row_index == numRows - 1:
                direction = -1
            elif row_index == 0:
                direction = 1

            row_index += direction

        chars = []
        for row in rows:
            chars.extend(row)
        return "".join(chars)
