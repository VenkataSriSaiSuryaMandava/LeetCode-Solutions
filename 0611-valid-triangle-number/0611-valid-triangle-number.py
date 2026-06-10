class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        res = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                l = j + 1
                r = n - 1

                while l <= r:
                    m = (l + r) // 2

                    if nums[i] + nums[j] > nums[m]:
                        l = m + 1
                    else:
                        r = m - 1
                
                res += (l - (j + 1))
        
        return res