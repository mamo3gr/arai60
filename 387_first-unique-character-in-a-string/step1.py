class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_index = dict()
        duplicate_chars = set()
        for i, c in enumerate(s):
            if c in duplicate_chars:
                if c in char_to_index:
                    del char_to_index[c]
                continue

            char_to_index[c] = i
            duplicate_chars.add(c)

        if not char_to_index:
            return -1

        return next(iter(char_to_index.values()))
