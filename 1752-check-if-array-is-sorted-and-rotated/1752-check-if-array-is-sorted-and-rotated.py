class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sortedNums = sorted(nums)

        for i in range(n):
            isSorted = True

            for j in range(n):
                if sortedNums[j] != nums[(i + j) % n]:
                    isSorted = False
            
            if isSorted:
                return True

        return False