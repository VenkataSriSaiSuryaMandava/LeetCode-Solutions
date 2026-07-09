class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[ : : -1]
        b = b[ : : -1]

        res = []
        carry = 0

        i = 0
        j = 0

        while i < len(a) or j < len(b) or carry:
            aVal = int(a[i]) if i < len(a) else 0
            bVal = int(b[j]) if j < len(b) else 0

            i += 1
            j += 1

            total = aVal + bVal + carry
            res.append(str(total % 2))
            carry = total // 2
        
        return "".join(res[ : : -1])