class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda p : p[1])

        res = 1
        end = pairs[0][1]

        for i in range(1, len(pairs)):
            if end < pairs[i][0]:
                end = pairs[i][1]
                res += 1
        
        return res