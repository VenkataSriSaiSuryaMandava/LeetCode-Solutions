class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        res = []
        last = {}

        for c in s:
            if c in last and len(res) - last[c] <= k:
                continue
                
            res.append(c)
            last[c] = len(res) - 1

        return "".join(res)