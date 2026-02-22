class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit = 0

        for ch in s:
            val = ord(ch) - ord('a') + 1
            digit += val % 10 + val // 10

        for i in range(k - 1):
            total = 0
            while digit:
                total += digit % 10
                digit = digit // 10
            digit = total
        
        return digit