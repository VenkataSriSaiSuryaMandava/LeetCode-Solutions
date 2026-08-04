class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        countT = defaultdict(int)
        countS = defaultdict(int)
        
        for ch in t:
            countT[ch] += 1
        
        need = len(countT)
        have = 0

        res = [0, 0]
        resLen = float("inf")

        l = 0

        for r, ch in enumerate(s):
            countS[ch] += 1

            if ch in countT and countT[ch] == countS[ch]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                countS[s[l]] -= 1
                
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res

        return s[l : r + 1] if res != float("inf") else ""
