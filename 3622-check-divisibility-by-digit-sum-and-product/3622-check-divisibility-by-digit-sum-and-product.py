class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digiSum = 0
        digiProduct = 1
        num = n

        while num:
            digit = num % 10
            num //= 10

            digiSum += digit
            digiProduct *= digit
        
        return n % (digiSum + digiProduct) == 0