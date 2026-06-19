class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        altitude = 0

        for netGain in gain:
            altitude += netGain
            res = max(res, altitude)
        
        return res