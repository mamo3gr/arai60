class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        row = 0
        going_down = True
        for c in s:
            rows[row].append(c)

            if going_down:
                row += 1
                if row == numRows - 1:
                    going_down = False
            else:
                row -= 1
                if row == 0:
                    going_down = True

        chars = []
        for r in rows:
            chars.extend(r)
        return "".join(chars)

    def convertGenerator(self, s: str, numRows: int) -> str:
        """
        Generatorでrow_indexを送り込むパターン。
        whileループで次のインデックスを計算するとやや煩雑に見えるので、
        Generatorで外に押し出せると見通しが良くなる。

        inspired from:
        https://github.com/saagchicken/coding_practice/pull/22
        """
        if numRows == 1:
            return s

        def row_index_gen(num_rows: int):
            row_index = 0
            while True:
                while row_index < num_rows - 1:
                    yield row_index
                    row_index += 1
                while row_index > 0:
                    yield row_index
                    row_index -= 1

        rows = [[] for _ in range(numRows)]
        for c, i in zip(s, row_index_gen(numRows)):
            rows[i].append(c)

        chars = []
        for r in rows:
            chars.extend(r)
        return "".join(chars)
