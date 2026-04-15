class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for c in s:
            if c == ']':
                cur = ""

                while stack[-1] != '[':
                    cur = stack.pop() + cur
                
                stack.pop()

                digit = ""
                while stack and stack[-1] in "0123456789":
                    digit = stack.pop() + digit
                
                stack.append(cur * int(digit))
            else:
                stack.append(c)
        
        return "".join(stack)