class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))

        while l <= r:
            s = l * l + r * r

            if c > s:
                l += 1
            elif c < s:
                r -= 1
            else:
                return True
        
        return False