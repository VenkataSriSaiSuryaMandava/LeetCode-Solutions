class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        res = 0
        count = 0

        l = 0
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            
            if (r - l + 1) == k:
                res = max(res, count)
                if s[l] in vowels:
                    count -= 1
                l += 1
        
        return res