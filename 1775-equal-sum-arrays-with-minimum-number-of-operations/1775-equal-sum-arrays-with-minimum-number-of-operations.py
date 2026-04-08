class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if sum1 == sum2:
            return 0

        if sum1 > sum2:
            return self.minOperations(nums2, nums1)
        
        diff = sum2 - sum1

        changes = []
        for val in nums1:
            changes.append(6 - val)
        
        for val in nums2:
            changes.append(val - 1)
        
        for count, val in enumerate(sorted(changes, reverse = True), 1):
            diff -= val

            if diff <= 0:
                return count
        
        return -1