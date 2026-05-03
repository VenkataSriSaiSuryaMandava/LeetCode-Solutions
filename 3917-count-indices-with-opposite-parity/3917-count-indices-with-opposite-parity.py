class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n

        even_count = 0
        odd_count = 0

        for i in range(n - 1, -1, -1):
            if nums[i] % 2:
                res[i] = even_count
                odd_count += 1
            else:
                res[i] = odd_count
                even_count += 1

        return res