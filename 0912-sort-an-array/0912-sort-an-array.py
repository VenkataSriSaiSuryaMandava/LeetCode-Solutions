class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        
        m = len(nums) // 2

        left = self.sortArray(nums[ : m])
        right = self.sortArray(nums[m : ])
        return self.merge(left, right)
    
    def merge(self, left, right):
        res = []
        
        l = 0
        r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        
        while l < len(left):
            res.append(left[l])
            l += 1
        
        while r < len(right):
            res.append(right[r])
            r += 1
        
        return res