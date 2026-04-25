class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        contains = False
        original = n
        
        while n:
            if n % 10 == x:
                contains = True
            n = n // 10

        while original >= 10:
            original = original // 10

        firstDigit = original

        return contains and firstDigit != x