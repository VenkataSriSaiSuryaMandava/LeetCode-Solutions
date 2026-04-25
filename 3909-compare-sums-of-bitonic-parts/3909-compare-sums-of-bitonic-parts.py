class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        r = len(nums) - 2

        while l <= r:
            m = (l + r) // 2

            if nums[m - 1] < nums[m] < nums[m + 1]:
                l = m + 1
            elif nums[m - 1] > nums[m] > nums[m + 1]:
                r = m - 1
            else:
                break

        leftSum = sum(nums[ : m + 1])
        rightSum = sum(nums[m : ])

        if leftSum > rightSum:
            return 0
        elif rightSum > leftSum:
            return 1
        else:
            return -1