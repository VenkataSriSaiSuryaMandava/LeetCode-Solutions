class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sortedNums = sorted(nums)

        for n in nums:
            l = 0
            r = len(sortedNums) - 1

            while l <= r:
                m = (l + r) // 2

                if n <= sortedNums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            res.append(l)
        
        return res