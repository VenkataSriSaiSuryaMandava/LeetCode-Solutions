class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 1
        r = len(arr) - 2

        while l <= r:
            m = (l + r) // 2

            if arr[m - 1] < arr[m] < arr[m + 1]:
                l = m + 1
            elif arr[m - 1] > arr[m] > arr[m + 1]:
                r = m - 1
            else:
                return m