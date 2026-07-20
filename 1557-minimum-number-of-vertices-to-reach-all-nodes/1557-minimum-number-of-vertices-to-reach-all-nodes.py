class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        count = {i : 0 for i in range(n)}
        res = []

        for src, dst in edges:
            count[dst] += 1
        
        for node, edge in count.items():
            if edge == 0:
                res.append(node)
        
        return res