class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        newX = 0

        while num:
            val = num % 10
            newX = newX * 10 + val
            num = num // 10
        
        if x < 0:
            newX *= -1
            
        if -(2 ** 31) <= newX <= (2 ** 31) -1:
            return newX
        else:
            return 0