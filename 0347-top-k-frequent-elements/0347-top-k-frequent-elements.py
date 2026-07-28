class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        heap = []

        for num, cnt in count.items():
            heapq.heappush(heap, [-cnt, num])
        
        res = []

        while len(res) < k:
            cnt, num = heapq.heappop(heap)
            res.append(num)
        
        return res