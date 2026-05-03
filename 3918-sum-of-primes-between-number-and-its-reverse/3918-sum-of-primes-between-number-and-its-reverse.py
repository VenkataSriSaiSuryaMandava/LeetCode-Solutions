class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = 0
        num = n
        
        while num:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10

        left = min(rev, n)
        right = max(rev, n)

        is_prime = [True] * (right + 1)
        
        if right >= 0:
            is_prime[0] = False

        if right >= 1:
            is_prime[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        res = 0
        for i in range(left, right + 1):
            if is_prime[i]:
                res += i

        return res