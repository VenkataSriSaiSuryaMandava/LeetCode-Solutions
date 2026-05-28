class Trie:
    def __init__(self):
        self.children = {}
        self.length = float("inf")
        self.idx = float("inf")
    
    def insert(self, word, index):
        node = self

        if len(word) < node.length:
            node.length = len(word)
            node.idx = index
        
        for ch in word[ : : -1]:
            if ch not in node.children:
                node.children[ch] = Trie()

            node = node.children[ch]

            if len(word) < node.length:
                node.length = len(word)
                node.idx = index
    
    def query(self, word):
        node = self

        for ch in word[ : : - 1]:
            if ch not in node.children:
                break
            
            node = node.children[ch]
        
        return node.idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()

        for i, word in enumerate(wordsContainer):
            trie.insert(word, i)
        
        return [trie.query(word) for word in wordsQuery]