class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        c in sについてtの先頭からマッチする、という考え方が自然に思えるが、
        マッチした後にしろ前にしろ、t_i をインクリメントするのが少しトリッキーに感じる。
        """
        t_i = -1  # start index to search for c in t
        for c in s:
            t_i += 1
            while t_i < len(t) and t[t_i] != c:
                t_i += 1
            if t_i == len(t):
                return False

        return True

    def isSubsequenceTwoPointers(self, s: str, t: str) -> bool:
        """
        これが一番しっくりきた。
        """
        s_i = 0
        t_i = 0
        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                s_i += 1
                t_i += 1
            else:
                t_i += 1

        reach_end_of_s = s_i == len(s)
        return reach_end_of_s
