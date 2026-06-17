class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        current_len = 0
        
        for i, ch in enumerate(s):
            if ch.islower():
                current_len += 1
            elif ch == '*':
                current_len = max(0, current_len - 1)
            elif ch == '#':
                current_len *= 2
            elif ch == '%':
                pass
            lengths[i] = current_len
            
        if k >= current_len or k < 0:
            return '.'
            
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0
            
            if ch == '*':
                continue
            elif ch == '#':
                if k >= prev_len:
                    k %= prev_len
            elif ch == '%':
                k = lengths[i] - 1 - k
            elif ch.islower():
                if k == lengths[i] - 1:
                    return ch
                    
        return '.'