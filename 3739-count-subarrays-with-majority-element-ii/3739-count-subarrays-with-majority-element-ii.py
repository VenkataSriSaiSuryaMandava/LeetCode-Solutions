class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = [0]
        pre = 0
        
        for num in nums:
            pre += 1 if num == target else -1
            prefix.append(pre)

        res = 0
        seen = []

        for prefix_sum in prefix:
            idx = bisect.bisect_left(seen, prefix_sum)
            res += idx
            bisect.insort(seen, prefix_sum)
        
        return res