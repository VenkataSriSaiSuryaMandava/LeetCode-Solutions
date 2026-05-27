class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        capIdx = {}
        smallIdx = {}

        for i, ch in enumerate(word):
            if ord('a') <= ord(ch) <= ord('z'):
                smallIdx[ord(ch) - ord('a')] = i
            else:
                if ord(ch) - ord('A') not in capIdx:
                    capIdx[ord(ch) - ord('A')] = i
        
        res = 0

        for ch, idx in smallIdx.items():
            if ch in capIdx and idx < capIdx[ch]:
                res += 1
        
        return res