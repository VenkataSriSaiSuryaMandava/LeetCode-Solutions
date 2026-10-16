class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_up(node: int) -> None:
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD
            
        def apply(node: int, l: int, r: int, val: int) -> None:
            length = r - l + 1
            tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + val * val % MOD * length) % MOD
            tree_sum[node] = (tree_sum[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD
            
        def push_down(node: int, l: int, r: int) -> None:
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0
                
        def update(node: int, l: int, r: int, ql: int, qr: int, val: int) -> None:
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
            push_up(node)
            
        last_pos = {}
        total_ans = 0
        
        for i, val in enumerate(nums):
            prev = last_pos.get(val, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            last_pos[val] = i
            total_ans = (total_ans + tree_sq[1]) % MOD
            
        return total_ans