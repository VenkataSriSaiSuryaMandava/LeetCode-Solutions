class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            curGene, curDepth = queue.popleft()

            if curGene == endGene:
                return curDepth
            
            for nextGene in bank:
                difference = sum(char1 != char2 for char1, char2 in zip(curGene, nextGene))

                if difference == 1 and nextGene not in visited:
                    queue.append((nextGene, curDepth + 1))
                    visited.add(nextGene)
        
        return -1