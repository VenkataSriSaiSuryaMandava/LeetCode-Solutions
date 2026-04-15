class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [[p, s] for p, s in zip(position, speed)]
        sortedpairs = sorted(pairs)[ : : -1]
        stack = []

        for p, s in sortedpairs:
            stack.append(float(target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)