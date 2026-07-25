class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        res = 0

        while n:
            digits.append(n % 10)
            n = n // 10
        
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                res = max(res, digits[i] * digits[j])

        return res