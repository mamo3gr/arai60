import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        normalized_to_words = collections.defaultdict(list)
        for word in strs:
            normalized = ''.join(sorted(word))
            normalized_to_words[normalized].append(word)
        
        return list(normalized_to_words.values())
