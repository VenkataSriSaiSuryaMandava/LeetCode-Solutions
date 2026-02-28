class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "aeiouAEIOU"

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            
            while l < r and s[r] not in vowels:
                r -= 1
            
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)