class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                cur = ""

                while stack[-1] != '[':
                    cur = stack.pop() + cur
                
                stack.pop()
                k = ""

                while stack and stack[-1] in "0123456789":
                    k = stack.pop() + k
                
                stack.append(cur * int(k))
        
        return "".join(stack)