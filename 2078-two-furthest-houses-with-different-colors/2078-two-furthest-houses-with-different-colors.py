class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        res = 0
        n = len(colors)
        
        for i in range(n):
            if colors[i] != colors[-1]:
                res = max(res, n - 1 - i)
  
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                res = max(res, i)
        
        return res