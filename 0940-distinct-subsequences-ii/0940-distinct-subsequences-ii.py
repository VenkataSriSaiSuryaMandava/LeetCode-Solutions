class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        endsWith = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            total = 0

            for cnt in endsWith:
                total += cnt
            
            endsWith[idx] = (total + 1) % MOD
        
        return sum(endsWith) % MOD