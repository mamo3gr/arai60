import collections


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        str.startswithがtuple[str]を受け取れることを利用して、
        同じ文字数の単語をまとめてチェックするバージョン。
        局所的な最適化で、ここまでやらなくてもよいと思う
        """

        # examine to whether s[i:] starts with any word in wordDict
        frontier = [0]
        visited = set()

        length_to_words = self.words_by_length(wordDict)

        while frontier:
            start = frontier.pop()
            if len(s) <= start:
                return True

            for length, words in length_to_words.items():
                new_start = start + length
                if new_start in visited:
                    continue
                if s.startswith(words, start):
                    frontier.append(new_start)
                    visited.add(new_start)

        return False

    @staticmethod
    def words_by_length(words: list[str]) -> dict[int, tuple[str]]:
        length_to_words = collections.defaultdict(list)
        for word in words:
            length_to_words[len(word)].append(word)

        return {length: tuple(words) for length, words in length_to_words.items()}
