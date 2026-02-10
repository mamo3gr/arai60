class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start_i = 0
        unique_chars = set()
        max_length = 0
        for i, c in enumerate(s):
            if c in unique_chars:
                length = i - start_i
                max_length = max(max_length, length)
                while start_i < i and c in unique_chars:
                    unique_chars.remove(s[start_i])
                    start_i += 1
            unique_chars.add(c)

        length = (i + 1) - start_i
        max_length = max(max_length, length)

        return max_length
