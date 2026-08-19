class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        res = ""

        for count, ch in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if count:
                heapq.heappush(heap, (count, ch))
        
        while heap:
            count1, ch1 = heapq.heappop(heap)

            if len(res) > 1 and res[-2] == res[-1] == ch1:
                if not heap:
                    break
                
                count2, ch2 = heapq.heappop(heap)
                res += ch2
                count2 += 1

                if count2 < 0:
                    heapq.heappush(heap, (count2, ch2))
            else:
                res += ch1
                count1 += 1
            
            if count1 < 0:
                heapq.heappush(heap, (count1, ch1))
        
        return res