class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit = x ^ y
        count = 0

        while bit:
            if bit & 1:
                count += 1
            bit = bit >> 1

        return count 