class Solution:
    def isPossible(self, target: List[int]) -> bool:
        curSum = sum(target)
        heap = []

        for num in target:
            heapq.heappush(heap, -1 * num)

        while -1 * heap[0] > 1:
            curNum = -1 * heapq.heappop(heap)
            remSum = curSum - curNum

            if remSum == 0 or curNum - remSum < 1:
                return False
            
            if curNum % remSum == 0:
                prevNum = remSum
            else:
                prevNum = curNum % remSum
            
            heapq.heappush(heap, -1 * prevNum)
            curSum += prevNum - curNum
        
        return True