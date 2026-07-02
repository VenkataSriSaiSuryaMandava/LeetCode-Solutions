class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        l = 0

        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)

            if r - l + 1 == k:
                if l > queue[0]:
                    queue.popleft()
                
                res.append(nums[queue[0]])
                l += 1
            
        return res