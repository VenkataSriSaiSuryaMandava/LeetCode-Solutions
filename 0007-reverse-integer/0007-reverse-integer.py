class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)
        newX = 0
        while x:
            val = x % 10
            newX = newX * 10 + val
            x = x // 10
        
        newX = newX * sign
        if -(2 ** 31) <= newX <= (2 ** 31) -1:
            return newX
        else:
            return 0