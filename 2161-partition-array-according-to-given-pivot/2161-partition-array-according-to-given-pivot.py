class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [pivot] * n

        i = 0
        j = n - 1

        l = 0
        r = n - 1

        while i < n:
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1
            
            if nums[j] > pivot:
                res[r] = nums[j]
                r -= 1
            
            i += 1
            j -= 1
        
        return res