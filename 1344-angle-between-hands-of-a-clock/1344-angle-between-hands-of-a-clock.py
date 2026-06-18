class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minDeg = minutes * 6
        hrDeg = hour * 30 + minutes * 0.5 
        diff = abs(minDeg - hrDeg)

        return min(diff, 360 - diff)