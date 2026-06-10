class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        max_log = int(math.log2(n)) + 1
        st_max = [[0] * max_log for _ in range(n)]
        st_min = [[0] * max_log for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, max_log):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j - 1], st_max[i + (1 << (j - 1))][j - 1])
                st_min[i][j] = min(st_min[i][j - 1], st_min[i + (1 << (j - 1))][j - 1])
                
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1
            
        def query_value(l: int, r: int) -> int:
            length = r - l + 1
            j = lg[length]
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        max_heap = []
        for l in range(n):
            val = query_value(l, n - 1)
            heappush(max_heap, (-val, l, n - 1))
            
        total_value = 0
        for _ in range(k):
            neg_val, l, r = heappop(max_heap)
            total_value += -neg_val
            
            if r > l:
                next_val = query_value(l, r - 1)
                heappush(max_heap, (-next_val, l, r - 1))
                
        return total_value