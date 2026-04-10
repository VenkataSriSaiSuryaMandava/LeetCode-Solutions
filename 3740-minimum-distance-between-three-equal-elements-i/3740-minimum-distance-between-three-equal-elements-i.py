class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf")
        indexes = defaultdict(list)

        for i, num in enumerate(nums):
            indexes[num].append(i)
        
        for num, idx in indexes.items():
            if len(idx) >= 3:
                for i in range(len(idx) - 2):
                    a = idx[i]
                    b = idx[i + 1]
                    c = idx[i + 2]

                    dist = abs(a - b) + abs(b - c) + abs(c - a)
                    res = min(res, dist)
        
        return -1 if res == float("inf") else res