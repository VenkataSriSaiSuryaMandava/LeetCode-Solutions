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
        nei = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[ : i] + "*" + word[i + 1: ]
                nei[pattern].append(word)

        res = 1
        visit = set(beginWord)
        queue = deque([beginWord])

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[ : j] + "*" + word[j + 1 : ]

                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            queue.append(neiWord)
                
            res += 1
        
        return 0