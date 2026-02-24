class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bit = 1
        
        while bit < n:
            bit = bit << 1

        return bit == n