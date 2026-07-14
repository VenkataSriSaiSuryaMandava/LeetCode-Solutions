class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for employee, manager in enumerate(manager):
            adj[manager].append(employee)
        
        def dfs(manager):
            res = 0

            for employee in adj[manager]:
                res = max(res, dfs(employee) + informTime[manager])
            
            return res
        
        return dfs(headID)