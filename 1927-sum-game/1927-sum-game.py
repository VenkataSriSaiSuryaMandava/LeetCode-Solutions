class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_l = sum(int(c) for c in num[:half] if c != '?')
        cnt_l = num[:half].count('?')
        
        sum_r = sum(int(c) for c in num[half:] if c != '?')
        cnt_r = num[half:].count('?')
        
        return 2 * (sum_l - sum_r) != 9 * (cnt_r - cnt_l)