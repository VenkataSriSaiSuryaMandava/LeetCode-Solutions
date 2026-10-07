class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        res = 0
        count = 0

        for box, units in boxTypes:
            if count + box <= truckSize:
                count += box
                res += box * units
            else:
                remaining = truckSize - count
                res += remaining * units
                break
        
        return res