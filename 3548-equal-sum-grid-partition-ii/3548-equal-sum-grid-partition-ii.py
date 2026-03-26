class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g):
            m, n = len(g), len(g[0])
            if m < 2: 
                return False

            bot_freq = Counter()
            for r in range(m):
                for c in range(n): 
                    bot_freq[g[r][c]] += 1

            top_freq = Counter()
            row_sums = [sum(row) for row in g]

            tot = sum(row_sums)
            top_sum = 0

            for r in range(1, m):
                for c in range(n):
                    v = g[r-1][c]
                    top_freq[v] += 1
                    bot_freq[v] -= 1

                    if bot_freq[v] == 0: 
                        del bot_freq[v]

                top_sum += row_sums[r-1]
                bot_sum = tot - top_sum

                if top_sum == bot_sum: 
                    return True

                diff = abs(top_sum - bot_sum)
                if top_sum > bot_sum:
                    if r == 1:
                        if diff == g[0][0] or diff == g[0][n-1]: 
                            return True
                    elif n == 1:
                        if diff == g[0][0] or diff == g[r-1][0]: 
                            return True
                    elif diff in top_freq: 
                        return True
                else:
                    bot_rows = m - r
                    if bot_rows == 1:
                        if diff == g[r][0] or diff == g[r][n-1]: 
                            return True
                    elif n == 1:
                        if diff == g[r][0] or diff == g[m-1][0]: 
                            return True
                    elif diff in bot_freq: 
                        return True
            return False
        
        if check(grid): 
            return True

        transposed = [[grid[r][c] for r in range(len(grid))] for c in range(len(grid[0]))]
        
        return check(transposed)