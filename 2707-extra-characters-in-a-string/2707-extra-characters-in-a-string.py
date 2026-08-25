class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        for word in words:
            cur = self.root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                
                cur = cur.children[c]
            
            cur.endOfWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root
        dp = {len(s) : 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            dp[i] = 1 + dfs(i + 1)
            cur = trie

            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                
                cur = cur.children[s[j]]

                if cur.endOfWord:
                    dp[i] = min(dp[i], dfs(j + 1))
            
            return dp[i]
        
        return dfs(0)