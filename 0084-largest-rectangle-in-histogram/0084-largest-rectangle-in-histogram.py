class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                prevIdx, prevHeight = stack.pop()
                res = max(res, (i - prevIdx) * prevHeight)
                start = prevIdx
            
            stack.append([start, h])
        
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        
        return res