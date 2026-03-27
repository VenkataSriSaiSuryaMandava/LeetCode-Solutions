class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0

        for i in range(2, n):
            tmp = i

            if primes[i]:
                tmp += i
                
                while tmp < n:
                    primes[tmp] = 0
                    tmp += i
        
        return sum(primes)