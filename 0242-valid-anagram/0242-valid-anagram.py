class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26

        for ch in s:
            count_s[ord(ch) - ord('a')] += 1
        
        for ch in t:
            count_t[ord(ch) - ord('a')] += 1
        
        return count_s == count_t