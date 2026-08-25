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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        rows = len(board)
        cols = len(board[0])

        visited = set()
        res = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(r, c, word, node):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visited or
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.endOfWord:
                res.add(word)
                node.endOfWord = False
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                backtrack(row, col, word, node)
            
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, "", root)
        
        return list(res)