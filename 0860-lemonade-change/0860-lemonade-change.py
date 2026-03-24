class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {5 : 0, 10 : 0, 20 : 0}

        for bill in bills:
            if bill == 5:
                coins[5] += 1
            elif bill == 10:
                coins[10] += 1
                if coins[5] == 0:
                    return False
                coins[5] -= 1
            elif bill == 20:
                coins[20] += 1
                if coins[10] == 0:
                    if coins[5] < 3:
                        return False
                    coins[5] -= 3
                else:
                    coins[10] -= 1
                    if coins[5] == 0:
                        return False
                    coins[5] -= 1
        
        return True