class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                k -= 1
            
            if k == 0:
                return i
        
        for i in range(int(sqrt(n)), 0, -1):
            if i * i == n:
                continue
            
            if n % i == 0:
                k -= 1
            
            if k == 0:
                return n / i

        return -1    