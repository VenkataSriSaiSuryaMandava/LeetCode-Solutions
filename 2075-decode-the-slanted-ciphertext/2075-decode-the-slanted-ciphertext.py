class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        res = []
        cols = len(encodedText) // rows

        for col in range(cols):
            r = 0
            c = col

            while r < rows and c < cols:
                idx = r * cols + c
                res.append(encodedText[idx])
                
                r += 1
                c += 1
        
        return "".join(res).rstrip()