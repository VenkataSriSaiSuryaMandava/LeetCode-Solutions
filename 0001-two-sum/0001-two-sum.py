class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differ = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in differ:
                return [differ[dif], i]
            differ[nums[i]] = i