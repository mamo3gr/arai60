class TrieNode:
    def __init__(self):
        self.char_to_child: dict[str, TrieNode] = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.char_to_child:
                node.char_to_child[char] = TrieNode()
            node = node.char_to_child[char]
        node.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        # whether s[:i] is breakable
        sentinel = [True]
        is_breakable = sentinel + [False] * len(s)

        for i in range(0, len(s)):
            if not is_breakable[i]:
                continue

            # confirm whether s[i:j+1] is breakable with trie
            node = trie.root
            for j in range(i, len(s)):
                char = s[j]
                if char not in node.char_to_child:
                    break
                node = node.char_to_child[char]
                if node.is_end:
                    is_breakable[j + 1] = True

        return is_breakable[-1]
