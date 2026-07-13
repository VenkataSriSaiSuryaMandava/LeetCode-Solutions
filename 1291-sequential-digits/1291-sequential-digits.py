class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for i in range(1, 9):
            number = i

            for j in range(i + 1, 10):
                number = number * 10 + j

                if low <= number <= high:
                    res.append(number)
        
        return sorted(res)