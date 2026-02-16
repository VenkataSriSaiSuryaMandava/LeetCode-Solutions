class Solution:
    def isBalanced(self, num: str) -> bool:
        count = 0
        for i in range(len(num)):
            if i % 2:
                count += int(num[i])
            else:
                count -= int(num[i])
                
        return count == 0