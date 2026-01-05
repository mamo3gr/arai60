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
        word_list = set()
        base_words = []
        for word in wordList:
            if word == endWord:
                base_words.append(word)
            else:
                word_list.add(word)

        if not base_words:
            return 0
        if len(base_words) >= 2:
            raise ValueError("There are duplicated words")

        num_hops = 0
        while base_words:
            num_hops += 1
            next_words = []

            for word_from in base_words:
                if self._is_pair(word_from, beginWord):
                    return num_hops + 1

                used_words = set()
                for word_to in word_list:
                    if not self._is_pair(word_from, word_to):
                        continue
                    next_words.append(word_to)
                    used_words.add(word_to)
                word_list -= used_words

            base_words = next_words

        return 0
