class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        curMax = -1

        for i, n in enumerate(arr):
            curMax = max(n, curMax)

            if i == curMax:
                res += 1
        
        return res