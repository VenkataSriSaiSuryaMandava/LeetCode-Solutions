class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        for ch in text:
            count[ch] += 1
        
        res = float("inf")
        for ch in "balon":
            if ch == 'l' or ch == "o":
                res = min(res, count[ch] // 2)
            res = min(res, count[ch])
        
        return res
