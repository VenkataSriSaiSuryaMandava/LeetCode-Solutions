class Solution:
    def numberOfWays(self, s: str) -> int:
        left = [0, 0]
        right = [s.count('0'), s.count('1')]

        res = 0

        for val in s:
            val = int(val)
            right[val] -= 1

            res += left[val ^ 1] * right[val ^ 1]

            left[val] += 1
        
        return res