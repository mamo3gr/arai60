import string


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        NOT_FOUND = -1
        # next_appearance[t_index][c] is the index
        # where c appears in t[t_index:]
        # NOTE: next_appearance[len(t)] is the sentinels
        next_appearance = [
            [NOT_FOUND] * len(string.ascii_lowercase) for _ in range(len(t) + 1)
        ]

        def char_to_index(c: str) -> int:
            assert len(c) == 1 and c in string.ascii_lowercase
            return ord(c) - ord("a")

        for c in string.ascii_lowercase:
            next_index = NOT_FOUND
            for i in reversed(range(len(t))):
                if t[i] == c:
                    next_index = i
                next_appearance[i][char_to_index(c)] = next_index

        """
        print(f't={t}')
        for c in string.ascii_lowercase:
            print(f'{c}: ', end='')
            for i in range(len(next_appearance)):
                print(next_appearance[i][char_to_index(c)], end=' ')
            print('')
        """

        t_index = 0
        for c in s:
            t_index = next_appearance[t_index][char_to_index(c)]
            if t_index == NOT_FOUND:
                return False
            t_index += 1

        return True
