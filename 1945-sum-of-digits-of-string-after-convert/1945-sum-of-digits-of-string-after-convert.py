class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = ""

        for ch in s:
            digits += str(ord(ch) - ord('a') + 1)
        
        digits = int(digits)
        for i in range(k):
            total = 0

            while digits:
                total += digits % 10
                digits = digits // 10
            
            digits = total
        
        return digits