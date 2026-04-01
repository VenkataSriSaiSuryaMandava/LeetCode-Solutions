class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n % 2:
            res = [0]
            n -= 1
        else:
            res = []
        
        i = 1
        while n:
            res = [-i] + res + [i]
            i += 1
            n -= 2
        
        return res