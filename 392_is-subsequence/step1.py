class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_i = 0
        for c in s:
            while t_i < len(t) and t[t_i] != c:
                t_i += 1
            if t_i >= len(t):
                return False
            t_i += 1

        return True
