class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([[startGene, 0]])
        visit = set([startGene])

        while queue:
            cur_gene, cur_depth = queue.popleft()

            if cur_gene == endGene:
                return cur_depth
            
            for next_gene in bank:
                difference = sum(char1 != char2 for char1, char2 in zip(cur_gene, next_gene))

                if difference == 1 and next_gene not in visit:
                    queue.append([next_gene, cur_depth + 1])
                    visit.add(next_gene)
        
        return -1