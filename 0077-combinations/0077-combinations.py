class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []

        def backtrack(i):
            if len(subset) == k:
                res.append(subset[ : :])
                return
            
            for j in range(i, n + 1):
                subset.append(j)
                backtrack(j + 1)
                subset.pop()
        
        backtrack(1)

        return res