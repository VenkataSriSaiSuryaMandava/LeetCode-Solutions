class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
        res = 0
        def check(x):
            y = 0
            temp = x
            k = 1

            while temp:
                digit = temp % 10

                if d[digit] == -1:
                    return False
                
                y = d[digit] * k + y
                temp = temp // 10
                k = k * 10
            
            return x != y

        for i in range(1, n + 1):
            if check(i):
                res += 1
        
        return res