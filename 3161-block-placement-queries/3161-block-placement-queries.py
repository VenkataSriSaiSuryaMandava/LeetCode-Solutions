import bisect

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node, start, mid, l, r),
                   self.query(2 * node + 1, mid + 1, end, l, r))

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        max_x = 0
        for q in queries:
            max_x = max(max_x, q[1])
        
        N = min(50001, max_x + 1)
        st = SegmentTree(N)
        obstacles = [0, 10**9]
        results = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obstacles, x)
                L = obstacles[idx - 1]
                R = obstacles[idx]
                
                bisect.insort(obstacles, x)
                st.update(1, 0, N, x, x - L)
                if R < N:
                    st.update(1, 0, N, R, R - x)
            else:
                x, sz = q[1], q[2]
                idx = bisect.bisect_left(obstacles, x)
                L = obstacles[idx - 1]
                
                max_gap = st.query(1, 0, N, 0, x)
                current_tail_gap = x - L
                results.append(max(max_gap, current_tail_gap) >= sz)
                
        return results