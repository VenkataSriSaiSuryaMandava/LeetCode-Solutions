from bisect import bisect_left

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        arr = sorted(zip(robots, distance))
        walls.sort()
        n = len(arr)
        cache = {}

        def count_walls(l, r):
            if l > r:
                return 0
            return bisect_left(walls, r + 1) - bisect_left(walls, l)

        def dfs(i, next_dir):
    
            if i < 0:
                return 0
            if (i, next_dir) in cache:
                return cache[(i, next_dir)]

            cur_pos, cur_dis = arr[i]

            left_start = cur_pos - cur_dis
            if i > 0:
                prev_pos = arr[i - 1][0]
                left_start = max(left_start, prev_pos + 1)

            take_left = count_walls(left_start, cur_pos) + dfs(i - 1, 0)

            right_end = cur_pos + cur_dis
            if i + 1 < n:
                next_pos, next_dis = arr[i + 1]
                if next_dir == 0:
                    right_end = min(right_end, next_pos - next_dis - 1)
                else:             
                    right_end = min(right_end, next_pos - 1)

            take_right = count_walls(cur_pos, right_end) + dfs(i - 1, 1)

            cache[(i, next_dir)] = max(take_left, take_right)
            return cache[(i, next_dir)]

        return max(dfs(n - 1, 0), dfs(n - 1, 1))