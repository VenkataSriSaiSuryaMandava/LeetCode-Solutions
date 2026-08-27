class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preMap = defaultdict(list)
        for pre, crs in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()

                for pre in preMap[crs]:
                    prereqMap[crs] |= dfs(pre)
                
                prereqMap[crs].add(crs)
            
            return prereqMap[crs]
        
        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for pre, crs in queries:
            res.append(pre in prereqMap[crs])
        
        return res