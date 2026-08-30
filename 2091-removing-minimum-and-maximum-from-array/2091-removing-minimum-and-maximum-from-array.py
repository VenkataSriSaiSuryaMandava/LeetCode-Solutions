class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minNum = min(nums)
        maxNum = max(nums)

        minIndex = nums.index(minNum)
        maxIndex = nums.index(maxNum)

        front = max(minIndex, maxIndex) + 1
        back = n - min(minIndex, maxIndex)
        frontAndBack = (min(minIndex, maxIndex) + 1) + (n - max(minIndex, maxIndex))

        return min(front, back, frontAndBack)