class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        res = len(text)

        for ch in text:
            count[ch] += 1
        
        for ch in "balon":
            if ch == "l" or ch == "o":
                res = min(res, count[ch] // 2)
            else:
                res = min(res, count[ch])
        
        return res