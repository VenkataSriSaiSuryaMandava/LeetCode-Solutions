class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        count = {}
        for v in freq.values():
            count[v] = 1 + count.get(v, 0)

        for x in nums:
            if count[freq[x]] == 1:
                return x

        return -1