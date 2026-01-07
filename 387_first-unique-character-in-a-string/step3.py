class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicated = set()
        unique_char_to_index = dict()
        for i, c in enumerate(s):
            if c in duplicated:
                continue
            if c in unique_char_to_index:
                del unique_char_to_index[c]
                duplicated.add(c)
                continue
            unique_char_to_index[c] = i

        if not unique_char_to_index:
            return -1

        return next(iter(unique_char_to_index.values()))
