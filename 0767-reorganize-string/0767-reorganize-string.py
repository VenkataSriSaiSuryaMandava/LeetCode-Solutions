class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)

        for ch in s:
            count[ch] += 1
        
        heap = [(-1 * cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(heap)

        res = ""
        prev = (0, "")

        while heap:
            cnt, ch = heapq.heappop(heap)
            res += ch

            if prev[0] < 0:
                heapq.heappush(heap, prev)
            
            prev = (cnt + 1,  ch)
        
        return res if len(res) == len(s) else ""