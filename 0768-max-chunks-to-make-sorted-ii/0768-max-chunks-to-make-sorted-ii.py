class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []

        for num in arr:
            if not stack or stack[-1] <= num:
                stack.append(num)
            else:
                max_num = stack.pop()

                while stack and stack[-1] > num:
                    stack.pop()
                
                stack.append(max_num)
        
        return len(stack)