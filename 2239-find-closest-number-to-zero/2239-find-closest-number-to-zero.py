class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, (abs(n), -1 * n))
        
        return -1 * minHeap[0][1]