class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        frontier = [s]
        visited = set()
        while frontier:
            query = frontier.pop()

            for word in wordDict:
                if not query.startswith(word):
                    continue

                reduced = query[len(word):]
                if reduced == "":
                    return True
                if reduced in visited:
                    continue

                frontier.append(reduced)
                visited.add(reduced)

        return False
