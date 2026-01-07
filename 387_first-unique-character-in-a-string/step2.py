class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_index = dict()
        for i, c in enumerate(s):
            if c in char_to_index:
                char_to_index[c] = -1
                continue

            char_to_index[c] = i

        for index in char_to_index.values():
            if index != -1:
                return index

        return -1
