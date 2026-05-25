class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        nums = sorted(list(set(nums)))

        earn1 = 0
        earn2 = 0

        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]

            temp = earn2

            if i > 0 and nums[i] == nums[i - 1] + 1:
                earn2 = max(earn2, earn1 + curEarn)
            else:
                earn2 += curEarn

            earn1 = temp
        
        return earn2