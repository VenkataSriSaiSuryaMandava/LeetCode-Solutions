class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        invert = False

        while length > 1:
            half = length // 2

            if k <= half:
                length = half
            elif k > half + 1:
                k = 1 + length - k
                length = half 
                invert = not invert
            else:
                if not invert:
                    return "1"
                else:
                    return '0'
        
        if not invert:
            return "0"
        else:
            return "1" 