class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indices = defaultdict(list)
        res = float("inf")

        for i, num in enumerate(nums):
            indices[num].append(i)
        
        for idx in indices.values():
            for i in range(len(idx) - 2):
                res = min(res, 2 * (idx[i + 2] - idx[i]))
        
        return -1 if res == float("inf") else res