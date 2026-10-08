class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            preMap[crs] = True
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True