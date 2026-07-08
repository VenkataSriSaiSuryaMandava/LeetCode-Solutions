class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        nz_digits = []
        nz_indices = []
        for i, ch in enumerate(s):
            if ch != '0':
                nz_digits.append(int(ch))
                nz_indices.append(i)
                
        k = len(nz_digits)
        
        pref_sum = [0] * (k + 1)
        P = [0] * (k + 1)
        pow10 = [1] * (k + 1)
        
        for i in range(k):
            pref_sum[i + 1] = pref_sum[i] + nz_digits[i]
            P[i + 1] = (P[i] * 10 + nz_digits[i]) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD
            
        next_nz = [k] * m
        prev_nz = [-1] * m
        
        ptr = 0
        for i in range(m):
            while ptr < k and nz_indices[ptr] < i:
                ptr += 1
            next_nz[i] = ptr
            
        ptr = k - 1
        for i in range(m - 1, -1, -1):
            while ptr >= 0 and nz_indices[ptr] > i:
                ptr -= 1
            prev_nz[i] = ptr
            
        res = []
        for l, r in queries:
            L = next_nz[l]
            R = prev_nz[r]
            
            if L > R:
                res.append(0)
                continue
            
            length = R - L + 1
            x = (P[R + 1] - P[L] * pow10[length]) % MOD
            digit_sum = pref_sum[R + 1] - pref_sum[L]
            
            res.append((x * digit_sum) % MOD)
            
        return res