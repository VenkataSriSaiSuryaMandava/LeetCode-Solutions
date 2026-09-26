class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=end=l=0
        d = {}
        while end < len(s):
            ch = s[end]
            if ch in d:
                start = max(start, d[ch]+1)
            d[ch] = end
            l = max(l, end-start+1)
            end += 1
        return max(l, end-start)
        
        