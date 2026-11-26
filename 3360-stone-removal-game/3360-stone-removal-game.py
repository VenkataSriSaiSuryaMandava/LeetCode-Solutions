class Solution:
    def canAliceWin(self, n: int) -> bool:
        Alice = True
        stone = 10

        while stone:
            if n - stone >= 0:
                    n -= stone
                    stone -= 1
                    Alice = not Alice
            else:
                return not Alice