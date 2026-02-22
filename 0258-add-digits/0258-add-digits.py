class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = self.sumOfDigits(num)
            
        return num
    
    def sumOfDigits(self, n):
        res = 0

        while n:
            res += n % 10
            n = n // 10
        
        return res