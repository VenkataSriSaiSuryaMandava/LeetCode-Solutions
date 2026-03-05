class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0

        for i in range(0, len(s), 2):
            if s[i] == '1':
                count1 += 1
            else:
                count2 += 1

            if i + 1 < len(s):
                if s[i + 1] == '0':
                    count1 += 1
                else:
                    count2 += 1
        
        return min(count1, count2)
            
            
        