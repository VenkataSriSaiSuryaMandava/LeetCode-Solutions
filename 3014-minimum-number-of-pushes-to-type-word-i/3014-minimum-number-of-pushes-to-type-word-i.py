class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        k = 1
        res = 0

        for i in range(n // 8):
            res += k * 8
            k += 1
        
        res += (n % 8) * k

        return res