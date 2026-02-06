class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        setNums = set(nums)

        for n in nums:
            cur = []
            if n - 1 not in setNums:
                count = 0
                while n + count in setNums:
                    cur.append(str(n + count))
                    count += 1
                if cur[0] == cur[-1]:
                    res.append(cur[0])
                else:
                    res.append(cur[0] + "->" + cur[-1])
        return res