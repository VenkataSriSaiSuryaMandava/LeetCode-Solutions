class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        setNums = set(nums)

        for n in nums:
            if n - 1 not in setNums:
                end = n
                while end + 1 in setNums:
                    end += 1
                if n == end:
                    res.append(str(n))
                else:
                    res.append(str(n) + "->" + str(end))
        return res