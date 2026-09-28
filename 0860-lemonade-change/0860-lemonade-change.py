class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = ten = 0

        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                if five >= 1:
                    five -= 1   
                else:
                    return False
            else:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
                