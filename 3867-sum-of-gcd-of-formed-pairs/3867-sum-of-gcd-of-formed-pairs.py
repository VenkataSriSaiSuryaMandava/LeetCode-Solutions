class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        prefixGcd = []
        maxNum = 0

        for num in nums:
            maxNum = max(maxNum, num)
            prefixGcd.append(gcd(maxNum, num))

        prefixGcd.sort()
        res = 0

        l = 0
        r = len(prefixGcd) - 1

        while l < r:
            res += gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        
        return res