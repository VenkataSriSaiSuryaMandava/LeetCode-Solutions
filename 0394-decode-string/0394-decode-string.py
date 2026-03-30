class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for ch in s:
            if ch == "]":
                encode_string = ""
                
                while stack[-1] != '[':
                    encode_string = stack.pop() + encode_string
                stack.pop()
                
                digit = ""
                while stack and stack[-1] in "0123456789":
                    digit = stack.pop() + digit

                digit = int(digit)
                encode_string *= digit

                stack.append(encode_string)

            else:
                stack.append(ch)
        
        return "".join(stack)