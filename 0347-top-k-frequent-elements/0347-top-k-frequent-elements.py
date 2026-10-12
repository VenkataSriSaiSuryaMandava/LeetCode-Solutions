class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        heap = []

        for num, cnt in count.items():
            heapq.heappush(heap, [-1 * cnt, num])
        
        res = []

        while len(res) < k:
            cnt, num = heapq.heappop(heap)
            res.append(num)
        
        return res