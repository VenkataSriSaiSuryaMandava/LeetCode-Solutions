class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()

                for pre in adj[crs]:
                    preMap[crs] |= dfs(pre)
                
                preMap[crs].add(crs)

            return preMap[crs]

        preMap = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for pre, crs in queries:
            res.append(pre in preMap[crs])
        
        return res