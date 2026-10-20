class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        def kmp_search(pattern: list[int], text: list[int]) -> bool:
            m = len(pattern)
            pi = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j
                
            j = 0
            for val in text:
                while j > 0 and val != pattern[j]:
                    j = pi[j - 1]
                if val == pattern[j]:
                    j += 1
                if j == m:
                    return True
            return False

        def is_valid(k: int) -> bool:
            for start in range(0, n, k):
                pattern = s[start : start + k]
                block = nums[start : start + k]
                text = block + block[:-1]
                if not kmp_search(pattern, text):
                    return False
            return True

        total_sum = 0
        for k in divisors:
            if is_valid(k):
                total_sum += k
                
        return total_sum