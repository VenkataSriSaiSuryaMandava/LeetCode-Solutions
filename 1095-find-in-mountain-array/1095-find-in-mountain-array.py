# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
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

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        l = peak
        r = length - 1

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        return -1
                