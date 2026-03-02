class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i > 0 and i < len(flowerbed) - 1:
                if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == 0:
                if flowerbed[i] == flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            
            if n <= 0:
                return True
        
        return False