class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        unique_chars = set()
        max_length = 0
        for end, c in enumerate(s):
            while c in unique_chars:
                unique_chars.remove(s[start])
                start += 1
            unique_chars.add(c)

            length = end - start + 1
            max_length = max(max_length, length)

        return max_length
