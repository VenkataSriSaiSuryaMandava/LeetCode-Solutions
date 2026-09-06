class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            d[key] += [s]
        res = []
        for val in d.values():
            res += [val]
        return res

        