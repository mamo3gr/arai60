import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_words: dict[str, List[str]] = collections.defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_to_words[sorted_word].append(word)

        return list(sorted_to_words.values())
