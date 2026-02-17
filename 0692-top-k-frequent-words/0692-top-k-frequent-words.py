class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        
        minheap = []
        for word, cnt in count.items():
            heapq.heappush(minheap, [-cnt, word])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        