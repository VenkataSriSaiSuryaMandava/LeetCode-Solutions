class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        r = x

        while l <= r:
            m = (l + r) // 2

            if x < m * m:
                r = m - 1
            elif x > m * m:
                l = m + 1
            else:
                return m
        return r