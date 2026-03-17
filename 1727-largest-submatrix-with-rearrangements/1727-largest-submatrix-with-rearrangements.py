class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        prev_heights = [0] * cols

        for r in range(rows):
            heights = matrix[r]

            for c in range(cols):
                if heights[c] > 0:
                    heights[c] += prev_heights[c]
            
            sorted_heights = sorted(heights, reverse = True)

            for i in range(cols):
                res = max(res, (i + 1) * sorted_heights[i])
            
            prev_heights = heights
        
        return res

