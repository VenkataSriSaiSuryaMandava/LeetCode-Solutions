class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' : '(' , ']' : '[' , '}' : '{'}
        stack = []

        for i in s:
            if i in pairs.values():
                stack.append(i)
            
            if i in pairs:
                if not stack or stack.pop() != pairs[i]:
                    return False
        return not stack