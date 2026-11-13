class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        dq = deque()
        
        for l in range(n - 1, -1, -1):
            cnt = 1
            while dq and dq[0][0] < nums[l]:
                val, c = dq.popleft()
                cost += (nums[l] - val) * c
                cnt += c
            dq.appendleft([nums[l], cnt])
            
            while cost > k:
                cost -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
                
            ans += r - l + 1
            
        return ans