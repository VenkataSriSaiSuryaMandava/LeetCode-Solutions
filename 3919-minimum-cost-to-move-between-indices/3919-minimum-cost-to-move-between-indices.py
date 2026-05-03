class Solution(object):
    def minCost(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        closest = [0] * n

        for i in range(n):
            if i == 0:
                closest[i] = 1
            elif i == n - 1:
                closest[i] = n - 2
            else:
                left = nums[i] - nums[i - 1]
                right = nums[i + 1] - nums[i]

                if left <= right:
                    closest[i] = i - 1
                else:
                    closest[i] = i + 1

        prefix = [0] * n
        for i in range(1, n):
            if closest[i - 1] == i:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1] + (nums[i] - nums[i - 1])

        suffix = [0] * n
        for i in range(n - 2, -1, -1):
            if closest[i + 1] == i:
                suffix[i] = suffix[i + 1] + 1
            else:
                suffix[i] = suffix[i + 1] + (nums[i + 1] - nums[i])

        res = []
        for l, r in queries:
            if l < r:
                res.append(prefix[r] - prefix[l])
            else:
                res.append(suffix[r] - suffix[l])

        return res