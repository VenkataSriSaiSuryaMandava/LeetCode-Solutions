class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs not in prereqmap:
                prereqmap[crs] = set()

                for pre in adj[crs]:
                    prereqmap[crs] |= dfs(pre)
                
                prereqmap[crs].add(crs)
            
            return prereqmap[crs]
        
        prereqmap = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for pre, crs in queries:
            res.append(pre in prereqmap[crs])
        
        return res
