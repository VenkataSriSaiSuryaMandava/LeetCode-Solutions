class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        revNum = 0
        num = n

        while num:
            digit = num % 10
            revNum = revNum * 10 + digit
            num = num // 10
        
        return abs(n - revNum)