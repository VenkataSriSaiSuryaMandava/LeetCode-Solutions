class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[ : i] + "*" + word[i + 1 : ]
                adj[pattern].append(word)
            
        visit = set([beginWord])
        queue = deque([beginWord])

        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[ : j] + "*" + word[j + 1 : ]

                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            
            res += 1

        return 0