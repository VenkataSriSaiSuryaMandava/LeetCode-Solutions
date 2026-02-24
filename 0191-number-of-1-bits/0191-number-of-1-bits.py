class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        bit = 1

        while n:
            count += bit & n
            n = n >> 1
        return count