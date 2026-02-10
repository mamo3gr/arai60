class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        char_to_index = dict()
        max_length = 0
        for end, c in enumerate(s):
            if c in char_to_index and char_to_index[c] >= start:
                start = char_to_index[c] + 1

            char_to_index[c] = end
            length = end - start + 1
            max_length = max(max_length, length)

        return max_length
