class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = defaultdict(int)
        dt = defaultdict(int)
        for i in s:
            ds[i] += 1
        for j in t:
            dt[j] += 1
        return dt == ds