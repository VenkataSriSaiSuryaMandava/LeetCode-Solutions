class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        num = x

        while x:
            reverse = reverse * 10 + x % 10
            x = x // 10
        
        return num == reverse