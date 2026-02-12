class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        countT = defaultdict(int)
        for c in t:
            countT[c] += 1
        need = len(countT)

        window = defaultdict(int)
        l = 0
        have = 0
        res = [-1, -1]
        reslen = float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        if reslen != float('inf'):
            return s[l : r + 1]
        else:
            return ""