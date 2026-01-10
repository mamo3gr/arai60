import collections
from typing import Iterable, Self


class NeighborWords:
    def __init__(self):
        self._subword_to_word = collections.defaultdict(list)

    @classmethod
    def from_words(cls, words: list[str]) -> Self:
        neighbor_words = NeighborWords()
        for word in words:
            neighbor_words.add(word)
        return neighbor_words

    @staticmethod
    def _to_subwords(word: str) -> Iterable[tuple[str, str]]:
        """dog -> (, og), (d, g), (do, )"""
        for i in range(len(word)):
            yield ((word[:i], word[i + 1 :]))

    def add(self, word: str) -> None:
        for subword in self._to_subwords(word):
            self._subword_to_word[subword].append(word)

    def iter_all(self, word: str) -> Iterable[str]:
        for subword in self._to_subwords(word):
            for neighbor in self._subword_to_word[subword]:
                yield neighbor


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbor_words = NeighborWords.from_words(wordList)
        to_visit = [beginWord]
        visited = set()
        sequence_length = 1
        while to_visit:
            next_to_visit = []

            for word in to_visit:
                if word == endWord:
                    return sequence_length

                for neighbor in neighbor_words.iter_all(word):
                    if neighbor in visited:
                        continue
                    next_to_visit.append(neighbor)
                    visited.add(neighbor)

            to_visit = next_to_visit
            sequence_length += 1

        return 0
