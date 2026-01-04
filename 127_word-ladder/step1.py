import collections


class Solution:
    @staticmethod
    def _is_pair(word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        num_different_chars = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                num_different_chars += 1

        return num_different_chars == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        base_indices = collections.deque()
        word_to_hops = [-1] * len(wordList)
        try:
            end_word_index = wordList.index(endWord)
            word_to_hops[end_word_index] = 1
            base_indices.append(end_word_index)
        except ValueError:
            return 0

        while True:
            next_indices = collections.deque()

            while base_indices:
                index_from = base_indices.popleft()
                word_from = wordList[index_from]
                if self._is_pair(word_from, beginWord):
                    return word_to_hops[index_from] + 1

                for i, word_to in enumerate(wordList):
                    if word_to_hops[i] > 0:
                        continue
                    if not self._is_pair(word_from, word_to):
                        continue
                    word_to_hops[i] = word_to_hops[index_from] + 1
                    next_indices.append(i)

            if not next_indices:
                return 0

            base_indices = next_indices
