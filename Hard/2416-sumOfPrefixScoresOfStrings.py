class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0  

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1 
    
    def get_score(self, word: str) -> int:
        node = self.root
        score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                score += node.prefix_count 
            else:
                break
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        result = []
        for word in words:
            result.append(trie.get_score(word))
        
        return result