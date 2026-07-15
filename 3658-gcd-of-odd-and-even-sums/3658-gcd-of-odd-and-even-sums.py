class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        sumOdd = n * n
        sumEven = n * (n + 1)

        return gcd(sumOdd, sumEven)