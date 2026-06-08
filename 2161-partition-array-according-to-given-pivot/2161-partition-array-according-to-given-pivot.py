class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        large = []
        count = 0

        for num in nums:
            if num > pivot:
                large.append(num)
            elif num < pivot:
                small.append(num)
            else:
                count += 1
        
        return small + [pivot] * count + large