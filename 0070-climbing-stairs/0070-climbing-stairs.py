class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = 1

        for i in range(n - 1):
            temp = first
            first = first + second
            second = temp
        
        return first