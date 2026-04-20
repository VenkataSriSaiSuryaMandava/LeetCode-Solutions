class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        nums = []
        for stone in stones:
            heapq.heappush(nums, -1 * stone) 

        while len(nums) > 1:
            x = -1 * heapq.heappop(nums)
            y = -1 * heapq.heappop(nums)

            if x != y:
                heapq.heappush(nums, -1 * abs(y - x))
        
        if stones:
            return -1 * nums[0]
        else:
            return 0