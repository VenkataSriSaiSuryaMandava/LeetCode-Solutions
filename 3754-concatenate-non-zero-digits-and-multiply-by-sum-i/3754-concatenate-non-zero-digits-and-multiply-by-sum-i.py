class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digitsSum = 0
        number = 0
        i = 0

        while n:
            digit = n % 10
            digitsSum += digit

            if digit:
                number = digit * (10 ** i) + number
                i += 1
            
            n = n // 10
        
        return number * digitsSum