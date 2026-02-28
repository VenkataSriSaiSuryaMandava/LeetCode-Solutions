class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = 0
        countMap = {0 : 1}

        for n in nums:
            prefixSum += n
            diff = prefixSum - k

            res += countMap.get(diff, 0)
            countMap[prefixSum] = 1 + countMap.get(prefixSum, 0)
        
        return res