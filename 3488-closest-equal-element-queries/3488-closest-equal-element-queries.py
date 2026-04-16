class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        m = 2 * n

        dist = [m] * m
        
        left = {}
        for i in range(m):
            x = nums[i % n]

            if x in left:
                dist[i] = min(dist[i], i - left[x])
            
            left[x] = i
        
        right = {}
        for i in range(m - 1, -1, -1):
            x = nums[i % n]

            if x in right:
                dist[i] = min(dist[i], right[x] - i)

            right[x] = i
        
        for i in range(n):
            dist[i] = min(dist[i], dist[i + n])
        
        res = []
        for q in queries:
            if dist[q] < n:
                res.append(dist[q])
            else:
                res.append(-1)
        
        return res