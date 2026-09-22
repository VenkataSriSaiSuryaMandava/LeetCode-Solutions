class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_count = [[0] * k for _ in range(4 * n)]

        def build(node: int, l: int, r: int):
            if l == r:
                rem = nums[l] % k
                tree_prod[node] = rem
                tree_count[node][rem] = 1
                return
            mid = (l + r) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            build(left_node, l, mid)
            build(right_node, mid + 1, r)
            
            p_left = tree_prod[left_node]
            p_right = tree_prod[right_node]
            tree_prod[node] = (p_left * p_right) % k
            
            cnt = list(tree_count[left_node])
            for rem, c in enumerate(tree_count[right_node]):
                if c:
                    cnt[(p_left * rem) % k] += c
            tree_count[node] = cnt

        def update(node: int, l: int, r: int, idx: int, val: int):
            if l == r:
                rem = val % k
                tree_prod[node] = rem
                tree_count[node] = [0] * k
                tree_count[node][rem] = 1
                return
            mid = (l + r) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            if idx <= mid:
                update(left_node, l, mid, idx, val)
            else:
                update(right_node, mid + 1, r, idx, val)
                
            p_left = tree_prod[left_node]
            p_right = tree_prod[right_node]
            tree_prod[node] = (p_left * p_right) % k
            
            cnt = list(tree_count[left_node])
            for rem, c in enumerate(tree_count[right_node]):
                if c:
                    cnt[(p_left * rem) % k] += c
            tree_count[node] = cnt

        def query(node: int, l: int, r: int, ql: int, qr: int):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_count[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * node, l, mid, ql, qr)
            if ql > mid:
                return query(2 * node + 1, mid + 1, r, ql, qr)
            
            p_left, cnt_left = query(2 * node, l, mid, ql, qr)
            p_right, cnt_right = query(2 * node + 1, mid + 1, r, ql, qr)
            
            merged_prod = (p_left * p_right) % k
            merged_cnt = list(cnt_left)
            for rem, c in enumerate(cnt_right):
                if c:
                    merged_cnt[(p_left * rem) % k] += c
            return merged_prod, merged_cnt

        build(1, 0, n - 1)
        ans = []
        for idx, val, start, x in queries:
            nums[idx] = val
            update(1, 0, n - 1, idx, val)
            _, counts = query(1, 0, n - 1, start, n - 1)
            ans.append(counts[x])
            
        return ans