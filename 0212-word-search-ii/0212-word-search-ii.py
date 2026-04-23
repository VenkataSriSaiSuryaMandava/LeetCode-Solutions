class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            
            cur = cur.children[c]
        
        cur.endOfWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = Trie()
        for word in words:
            root.addWord(word)
        
        rows = len(board)
        cols = len(board[0])
        
        res = set()
        visit = set()

        def backtrack(r, c, word, node):
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
                node.endOfWord = False

            backtrack(r + 1, c, word, node)
            backtrack(r - 1, c, word, node)
            backtrack(r, c + 1, word, node)
            backtrack(r, c - 1, word, node)
            
            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    backtrack(r, c, "", root)
        
        return list(res)