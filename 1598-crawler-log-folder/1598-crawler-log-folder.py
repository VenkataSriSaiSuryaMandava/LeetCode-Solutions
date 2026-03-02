class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for l in logs:
            if l == "../" and stack:
                stack.pop()
            elif l[0] != '.':
                stack.append(l[0])
        
        return len(stack)