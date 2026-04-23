class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = defaultdict(list)

        for i, num in enumerate(nums):
            count[num].append(i)
        
        res = [0] * len(nums)

        for idx in count.values():
            left = 0
            right = sum(idx) - idx[0] * len(idx)

            for i in range(len(idx)):
                res[idx[i]] = left + right

                if i + 1 < len(idx):
                    left += (idx[i + 1] - idx[i]) * (i + 1)
                    right -= (idx[i + 1] - idx[i]) * (len(idx) - i - 1)
        
        return res