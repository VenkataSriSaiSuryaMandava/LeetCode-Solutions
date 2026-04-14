class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
                
            if i == len(robot):
                return 0
            
            if j == len(factory):
                return float("inf")
            
            res = dfs(i, j + 1)
            dist = 0

            for k in range(factory[j][1]):
                if i + k == len(robot):
                    break
                
                dist += abs(robot[i + k] - factory[j][0])
                res = min(res, dist + dfs(i + k + 1, j + 1))
            
            cache[(i, j)] = res
            return res
        
        return dfs(0, 0)