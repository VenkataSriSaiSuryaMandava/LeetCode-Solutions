class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)
        b = b[2 : ]

        l = 0
        res = 0
        for r in range(len(b)):
            if b[r] == '1':
                res = max(res, r - l)
                l = r
        
        return res