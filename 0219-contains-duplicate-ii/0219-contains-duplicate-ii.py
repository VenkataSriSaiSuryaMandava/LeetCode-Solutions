class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indices = {}

        for i, num in enumerate(nums):
            if num in indices and i - indices[num] <= k:
                return True
            
            indices[num] = i
        
        return False