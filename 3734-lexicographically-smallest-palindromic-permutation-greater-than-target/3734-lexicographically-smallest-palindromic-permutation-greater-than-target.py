from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        
        odd_chars = [ch for ch, cnt in count.items() if cnt % 2 != 0]
        if len(odd_chars) > 1 or (n % 2 == 0 and len(odd_chars) > 0):
            return ""
        
        mid = odd_chars[0] if odd_chars else ""
        half_counts = Counter({ch: count[ch] // 2 for ch in count if count[ch] // 2 > 0})
        m = n // 2
        
        target_half = target[:m]
        target_half_counts = Counter(target_half)
        
        if all(half_counts[ch] >= target_half_counts[ch] for ch in target_half_counts):
            full_pal = target_half + mid + target_half[::-1]
            if full_pal > target:
                return full_pal
        
        pref_counts = Counter()
        for i in range(m):
            if i > 0:
                pref_counts[target[i - 1]] += 1
            
        for i in range(m - 1, -1, -1):
            if i < m - 1:
                pref_counts[target[i]] -= 1
                if pref_counts[target[i]] == 0:
                    del pref_counts[target[i]]
            
            if not all(half_counts[ch] >= pref_counts[ch] for ch in pref_counts):
                continue
            
            rem = half_counts - pref_counts
            valid_chars = sorted([ch for ch in rem if ch > target[i] and rem[ch] > 0])
            
            if valid_chars:
                chosen = valid_chars[0]
                rem[chosen] -= 1
                
                tail = []
                for ch in sorted(rem.keys()):
                    if rem[ch] > 0:
                        tail.append(ch * rem[ch])
                
                first_half = target[:i] + chosen + "".join(tail)
                return first_half + mid + first_half[::-1]
        
        return ""