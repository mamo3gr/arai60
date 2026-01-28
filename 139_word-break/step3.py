class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # examine to whether s[i:] starts with any word in wordDict
        frontier = [0]
        visited = set()

        while frontier:
            start = frontier.pop()
            if len(s) <= start:
                return True

            for word in wordDict:
                new_start = start + len(word)
                if new_start in visited:
                    continue
                if s.startswith(word, start):
                    frontier.append(new_start)
                    visited.add(new_start)

        return False
