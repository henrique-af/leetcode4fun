from typing import List


class Node:
    def __init__(self):
        self.edges = {}
        self.word_end = False


class Trie:
    def __init__(self, dictionary):
        self.root = Node()

        for word in dictionary:
            self.add(word)

    def add(self, word):
        node = self.root

        for c in word:
            if c not in node.edges:
                node.edges[c] = Node()
            node = node.edges[c]
        node.word_end = True

    def search(self, word):
        node = self.root

        ans = []
        for c in word:
            if c not in node.edges:
                return word
            ans.append(c)
            node = node.edges[c]
            if node.word_end:
                return "".join(ans)
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie(dictionary)
        ans = []
        for word in sentence.split():
            ans.append(t.search(word))
        return " ".join(ans)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
sol = Solution()
print(sol.replaceWords(dictionary, sentence))
