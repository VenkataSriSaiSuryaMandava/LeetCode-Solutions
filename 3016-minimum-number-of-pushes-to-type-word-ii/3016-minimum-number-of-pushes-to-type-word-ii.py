class Solution:
    def minimumPushes(self, word: str) -> int:
        count = defaultdict(int)
        res = 0

        for ch in word:
            count[ch] += 1
        
        for i, cnt in enumerate(sorted(count.values(), reverse = True)):
            res += (i // 8 + 1) * cnt
        
        return res