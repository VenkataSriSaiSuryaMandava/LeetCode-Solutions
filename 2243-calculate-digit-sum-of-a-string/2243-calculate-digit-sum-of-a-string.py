class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            newS = ""
            length = len(s)
            l = 0

            while l < length:
                curSum = 0

                for i in range(l, min(l + k, length)):
                    curSum += int(s[i])
                
                l += k
                newS += str(curSum)
            
            s = newS
        
        return s