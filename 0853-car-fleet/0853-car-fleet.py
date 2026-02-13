class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        sortedpairs = sorted(pairs)[::-1]
        stack = []

        for p, s in sortedpairs:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)