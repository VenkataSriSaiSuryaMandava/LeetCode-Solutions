class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        res = []
        visit = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res