class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if ch == '*':
                if res:
                    res.pop()
            elif ch == '#':
                res += res
            elif ch == '%':
                res = res[ : : -1]
            else:
                res.append(ch)
        
        return "".join(res)