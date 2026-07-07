class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []

        for ch in s:
            if ord('A') <= ord(ch) <= ord('Z'):
                res.append(chr(ord('a') + ord(ch) - ord('A')))
            else:
                res.append(ch)
        
        return "".join(res)