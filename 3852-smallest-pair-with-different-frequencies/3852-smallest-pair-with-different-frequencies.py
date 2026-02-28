class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        vals = sorted(freq.keys())
        
        for i in range(len(vals)):
            x_val = vals[i]
            for j in range(1, len(vals)):
                y_val = vals[j]
                if freq[x_val] != freq[y_val]:
                    return [x_val, y_val]

        return [-1, -1]