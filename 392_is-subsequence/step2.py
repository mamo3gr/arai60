class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        str.findを使うパターン
        """
        t_i = 0
        for c in s:
            t_i = t.find(c, t_i)
            if t_i == -1:
                return False

            t_i += 1

        return True

    def isSubsequenceIterator(self, s: str, t: str) -> bool:
        """
        イテレータを使って1文字づつ出力するパターン
        """
        it = iter(t)
        for c_s in s:
            try:
                while True:
                    c_t = next(it)
                    if c_t == c_s:
                        break
            except StopIteration:
                return False

        return True

    def isSubsequenceIterator2(self, s: str, t: str) -> bool:
        """
        Geminiに教えてもらった、イテレータを使った解法
        """
        it = iter(t)
        return all(c in it for c in s)

    def isSubsequenceBisect(self, s: str, t: str) -> bool:
        """
        フォローアップ問題の解答
        """
        import bisect
        import collections

        char_to_indices = collections.defaultdict(list)
        for i, c in enumerate(t):
            char_to_indices[c].append(i)

        t_i = -1
        for c in s:
            indices = char_to_indices[c]
            i = bisect.bisect_left(indices, t_i + 1)
            if i >= len(indices):
                return False
            t_i = indices[i]

        return True

    def isSubsequenceTwoPointers(self, s: str, t: str) -> bool:
        """
        inspired from:
        https://github.com/h1rosaka/arai60/pull/56
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

    def isSubsequenceRecursive(self, s: str, t: str) -> bool:
        """
        関数型っぽい見え方から、再帰的に書いてみたパターン
        """
        if not s:
            return True
        if not t:
            return False

        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])
