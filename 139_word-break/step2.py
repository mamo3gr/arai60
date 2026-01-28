class Solution:
    def wordBreakIndexDFS(self, s: str, wordDict: list[str]) -> bool:
        """
        sのどこまでbreakできたか、インデックスで保持するDFS.
        startやendなどインデックスの範囲に気を使う。
        """
        frontier = [0]  # s[:i] is breakable and examine whether s[i:] is breakable
        visited = {0}
        while frontier:
            start = frontier.pop()
            if start == len(s):
                return True

            for end in range(start, len(s) + 1):
                if end in visited:
                    continue
                if s[start:end] in wordDict:
                    frontier.append(end)
                    visited.add(end)

        return False

    def wordBreakDP(self, s: str, wordDict: list[str]) -> bool:
        """
        DPでの解法。
        内部ループはfor each 始点とfor each wordがある。ここでは前者。
        """
        word_dict = set(wordDict)

        sentinel = [True]
        is_breakable = sentinel + [False] * len(s)  # s[:i] is breakable

        for end in range(1, len(s) + 1):
            # examine whether s[:end] is breakable
            for begin in range(end):
                if is_breakable[begin] and s[begin:end] in word_dict:
                    is_breakable[end] = True
                    break

        return is_breakable[-1]
