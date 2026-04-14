class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s) or t == "":
            return ""
        
        countT = defaultdict(int)
        for ch in t:
            countT[ch] += 1
        
        need = len(countT)

        window = defaultdict(int)
        have = 0 
        res = [0, 0]
        reslen = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1


            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = [l, r]

                ch = s[l]
                window[ch] -= 1
                
                if ch in countT and countT[ch] > window[ch]:
                    have -= 1
                l += 1
        
        l, r = res

        if reslen == float("inf"):
            return ""
        else:
            return s[l : r + 1]
