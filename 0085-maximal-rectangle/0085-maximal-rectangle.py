class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        n = len(heights)

        res = 0

        for row in matrix:
            for i, h in enumerate(row):
                if h == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
        
            left = [-1] * n
            stack = []

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] >= h:
                    stack.pop()
                
                if stack:
                    left[i] = stack[-1]
                
                stack.append(i)
            
            right = [n] * n
            stack = []

            for i in range(n - 1, -1, -1):
                h = heights[i]

                while stack and heights[stack[-1]] >= h:
                    stack.pop()

                if stack:
                    right[i] = stack[-1]
                
                stack.append(i)

            for i, h in enumerate(heights):
                res = max(res, h * (right[i] - left[i] - 1))
        
        return res