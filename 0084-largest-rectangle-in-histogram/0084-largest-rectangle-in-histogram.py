class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                area = (i - index) * height
                res = max(res, area)
            stack.append([start, h])
        for i, h in stack:
            area = (len(heights) - i) * h
            res = max(res, area)
        return res