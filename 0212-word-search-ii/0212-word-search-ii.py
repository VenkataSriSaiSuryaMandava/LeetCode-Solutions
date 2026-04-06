class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        rows = len(board)
        cols = len(board[0])

        visit = set()
        res = set()

        def backtrack(r, c, node, word):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or
                board[r][c] not in node.children):
                return 
            
            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.endOfWord:
                res.add(word)
            
            backtrack(r + 1, c, node, word)
            backtrack(r - 1, c, node, word)
            backtrack(r, c + 1, node, word)
            backtrack(r, c - 1, node, word)

            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root, "")
        
        return list(res)