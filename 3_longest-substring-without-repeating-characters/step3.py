class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        char_to_index = dict()
        max_length = 0
        for end, c in enumerate(s):
            last_index_to_appear = char_to_index.get(c, -1)
            if start <= last_index_to_appear:
                start = last_index_to_appear + 1
            char_to_index[c] = end

            length = end - start + 1
            max_length = max(max_length, length)

        return max_length
