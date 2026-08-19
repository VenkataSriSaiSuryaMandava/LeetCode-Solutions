class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        
        minHeap = [(-1 * cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(minHeap)

        res = ""
        prev = (0, "")

        while minHeap:
            cnt, ch = heapq.heappop(minHeap)
            res += ch

            if prev[0] < 0:
                heapq.heappush(minHeap, prev)
            
            cnt += 1
            prev = (cnt, ch)
        
        return res if len(res) == len(s) else ""