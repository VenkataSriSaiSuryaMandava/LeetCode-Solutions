class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = []
        
        for i in range(1, n + 1):
            binary = bin(i)[2 : ]
            res.append(binary)

        binarystring = "".join(res)

        return int(binarystring, 2) % (10 ** 9 + 7)