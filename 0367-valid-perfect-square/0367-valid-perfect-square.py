class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num

        while l <= r:
            m = (l + r) // 2

            if num > m * m:
                l = m + 1
            elif num < m * m:
                r = m - 1
            else:
                return True
        
        return False