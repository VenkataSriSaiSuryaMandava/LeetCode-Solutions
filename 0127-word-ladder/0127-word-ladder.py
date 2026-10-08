class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        wordMap = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[ : i] + "*" + word[i + 1 : ]
                wordMap[pattern].append(word)
        
        queue = deque([beginWord])
        visited = {beginWord}
        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[ : j] + '*' + word[j + 1 : ]

                    for nextWord in wordMap[pattern]:
                        if nextWord not in visited:
                            visited.add(nextWord)
                            queue.append(nextWord)
            
            res += 1
        
        return 0