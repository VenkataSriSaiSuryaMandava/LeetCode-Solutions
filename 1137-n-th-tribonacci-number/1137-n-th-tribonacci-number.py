class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        seq = [0, 1, 1]

        if n < 3:
            return seq[n]
        
        for i in range(n - 2):
            temp = sum(seq)
            seq[0] = seq[1]
            seq[1] = seq[2]
            seq[2] = temp

        return seq[-1]

