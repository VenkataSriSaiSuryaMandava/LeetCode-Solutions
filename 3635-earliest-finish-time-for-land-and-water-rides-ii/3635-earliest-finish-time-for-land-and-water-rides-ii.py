class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def calc(a1, t1, a2, t2):
            min_end = min(a + t for a, t in zip(a1, t1))
            return min(max(min_end, a) + t for a, t in zip(a2, t2))
        
        land_then_water = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        water_then_land = calc(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_then_water, water_then_land)