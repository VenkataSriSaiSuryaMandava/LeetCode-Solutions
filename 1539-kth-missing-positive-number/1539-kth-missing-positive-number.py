class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            missing = arr[m] - (m + 1)

            if missing < k:
                l = m + 1
            else:
                r = m - 1
        
        return  l + k