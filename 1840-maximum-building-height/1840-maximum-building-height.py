class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)
        
        for i in range(1, m):
            id_prev, h_prev = restrictions[i - 1]
            id_curr, h_curr = restrictions[i]
            restrictions[i][1] = min(h_curr, h_prev + (id_curr - id_prev))
            
        for i in range(m - 2, -1, -1):
            id_next, h_next = restrictions[i + 1]
            id_curr, h_curr = restrictions[i]
            restrictions[i][1] = min(h_curr, h_next + (id_next - id_curr))
            
        max_overall_height = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_overall_height = max(max_overall_height, peak)
            
        return max_overall_height