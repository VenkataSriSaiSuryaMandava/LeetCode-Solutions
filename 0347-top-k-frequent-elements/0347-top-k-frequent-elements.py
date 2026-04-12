class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        minHeap = []
        for num, cnt in count.items():
            heapq.heappush(minHeap, [-cnt, num])
        
        res = []
        while k != len(res):
            cnt, num = heapq.heappop(minHeap)
            res.append(num)
        
        return res