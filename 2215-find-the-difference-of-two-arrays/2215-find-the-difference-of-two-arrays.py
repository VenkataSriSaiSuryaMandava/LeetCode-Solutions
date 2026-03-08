class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setNums1 = set(nums1)
        setNums2 = set(nums2)

        list1 = []
        for n in setNums1:
            if n not in setNums2:
                list1.append(n)
        
        list2 = []
        for n in setNums2:
            if n not in setNums1:
                list2.append(n)
        
        return [list1, list2]