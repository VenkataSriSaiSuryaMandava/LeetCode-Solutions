# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        length = mountainArr.length()

        l = 1
        r = length - 2

        while l <= r:
            m = (l + r) // 2

            left = mountainArr.get(m - 1)
            mid = mountainArr.get(m)
            right = mountainArr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        
        peak = m

        l = 0
        r = peak

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if target > val:
                l = m + 1
            elif target < val:
                r = m - 1
            else:
                return m
        
        l = peak
        r = length - 1

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if target < val:
                l = m + 1
            elif target > val:
                r = m - 1
            else:
                return m
        
        return -1
