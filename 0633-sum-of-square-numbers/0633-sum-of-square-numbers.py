class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))

        while l <= r:
            if c > l * l + r * r:
                l += 1
            elif c < l * l + r * r:
                r -= 1
            else:
                return True
        
        return False