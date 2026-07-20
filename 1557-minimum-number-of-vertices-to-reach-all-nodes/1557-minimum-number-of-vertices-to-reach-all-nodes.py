class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [0] * n
        res = []

        for src, dst in edges:
            count[dst] += 1
        
        for i, edge in enumerate(count):
            if edge == 0:
                res.append(i)
        
        return res