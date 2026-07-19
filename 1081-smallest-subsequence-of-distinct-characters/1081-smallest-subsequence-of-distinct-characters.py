class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIdx = {ch : i for i, ch in enumerate(s)}

        visited = set()
        stack = []

        for i, ch in enumerate(s):
            if ch in visited:
                continue
            
            while stack and stack[-1] > ch and lastIdx[stack[-1]] > i:
                visited.remove(stack.pop())
            
            stack.append(ch)
            visited.add(ch)
        
        return "".join(stack)