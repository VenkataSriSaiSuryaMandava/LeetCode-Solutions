class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]

        if n < 3:
            return t[n]

        for i in range(n - 2):
            t[0], t[1], t[2] = t[1], t[2], t[0] + t[1] + t[2]
        
        return t[2]