import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:  return []

        nums = Counter(nums)
        h = []
        res = []
        for key,v in nums.items():
            heapq.heappush(h, (-v,key))
        i=0
        while h and k>0:
            res.append(heapq.heappop(h)[1])
            k -= 1
        return res

        