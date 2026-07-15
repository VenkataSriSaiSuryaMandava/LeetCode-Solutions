class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        nei = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[ : i] + '*' + word[i + 1 : ]
                nei[pattern].append(word)

        queue = deque([(beginWord)])
        visited = set([beginWord])
        res = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[ : i] + '*' + word[i + 1 : ]

                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            queue.append(neiWord)

            res += 1
        
        return 0