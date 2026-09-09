class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        threshold = 1000

        while threshold <= n:
            res += n - threshold + 1
            threshold *= 1000
        
        return res