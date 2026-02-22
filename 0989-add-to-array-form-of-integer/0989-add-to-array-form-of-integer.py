class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[ : : -1]
        i = 0
        
        while k:
            if i < len(num):
                total = num[i] + k
                num[i] = total % 10
                k = total // 10
            else:
                num.append(k % 10)
                k = k // 10
            i += 1

        return num[ : : -1]