class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        numsSet = set(nums)

        smallest = min(nums)
        largest = max(nums)

        for num in range(smallest, largest + 1):
            if num not in numsSet:
                res.append(num)
        
        return res