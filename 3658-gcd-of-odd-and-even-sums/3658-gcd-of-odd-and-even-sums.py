class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        sumOdd = 0
        sumEven = 0

        for num in range(1, 2 * n, 2):
            sumOdd += num
            sumEven += num + 1

        return gcd(sumOdd, sumEven)