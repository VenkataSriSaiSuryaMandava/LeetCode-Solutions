class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [(-cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(maxheap)

        prev = (0, "")
        res = ""
        while maxheap:
            cnt, ch = heapq.heappop(maxheap)
            res += ch
            if prev[0] < 0:
                heapq.heappush(maxheap, prev)
            
            cnt += 1
            prev = (cnt, ch)

        if len(res) == len(s):
            return res
        else:
            return ""
            